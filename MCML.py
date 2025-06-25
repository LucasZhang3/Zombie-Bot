import torch
import cv2
import numpy as np
import pygetwindow as gw
import mss
import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter import ttk

pyautogui.FAILSAFE = False

model = torch.hub.load(
    'ultralytics/yolov5',
    'custom',
    path=r'YOUR PATH'
)
model.conf = 0.25

try:
    window = gw.getWindowsWithTitle("Minecraft")[0]
except IndexError:
    print("Minecraft window not found. Please start Minecraft.")
    exit(1)

window.restore()
window.activate()
time.sleep(0.5)

left, top = window.left, window.top
width, height = window.width, window.height
print(f"Window position and size: left={left}, top={top}, width={width}, height={height}")

sct = mss.mss()
monitor = {"top": top, "left": left, "width": width, "height": height}

running = False
delay_between_hits = 1.0  
distance_threshold = 50  
last_attack_time = 0


root = tk.Tk()
root.title("Minecraft Zombie Triggerbot")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Delay between hits (seconds):").grid(row=0, column=0, sticky='w')
delay_scale = ttk.Scale(frame, from_=0.1, to=5.0, orient='horizontal')
delay_scale.set(delay_between_hits)
delay_scale.grid(row=1, column=0, sticky='ew')

ttk.Label(frame, text="Distance threshold (pixels):").grid(row=2, column=0, sticky='w')
distance_scale = ttk.Scale(frame, from_=10, to=200, orient='horizontal')
distance_scale.set(distance_threshold)
distance_scale.grid(row=3, column=0, sticky='ew')

status_label = ttk.Label(frame, text="Status: Stopped")
status_label.grid(row=6, column=0, sticky='w', pady=(10, 0))

def update_delay(val):
    global delay_between_hits
    delay_between_hits = float(val)

def update_distance(val):
    global distance_threshold
    distance_threshold = int(float(val))  

delay_scale.config(command=update_delay)
distance_scale.config(command=update_distance)

def start_bot():
    global running
    if not running:
        running = True
        status_label.config(text="Status: Running")
        root.after(10, aimbot_loop)  

def stop_bot():
    global running
    running = False
    status_label.config(text="Status: Stopped")
    cv2.destroyAllWindows()

start_button = ttk.Button(frame, text="Start", command=start_bot)
start_button.grid(row=4, column=0, sticky='ew', pady=(10, 0))

stop_button = ttk.Button(frame, text="Stop", command=stop_bot)
stop_button.grid(row=5, column=0, sticky='ew', pady=(5, 0))

def aimbot_loop():
    global running, last_attack_time

    if not running:
        return

    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    results = model(img)
    boxes = results.xyxy[0].cpu().numpy()

    if len(boxes) > 0:
        best_box = max(boxes, key=lambda x: x[4])
        x1, y1, x2, y2, conf, cls = best_box

        if conf > 0.25:
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            center_x = width // 2
            center_y = height // 2

            dist = ((cx - center_x) ** 2 + (cy - center_y) ** 2) ** 0.5

            print(f"[AIM] Zombie at ({cx},{cy}), dist: {dist:.1f}, Conf: {conf:.2f}")

            now = time.time()
            if dist < distance_threshold and (now - last_attack_time) >= delay_between_hits:
                print("[AIMBOT] Attacking!")
                pyautogui.click(button='left')
                last_attack_time = now

    results.render()
    output = results.ims[0]
    cv2.imshow("Minecraft Detection", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_bot()
        root.quit()
        return

    root.after(10, aimbot_loop)

root.mainloop()
