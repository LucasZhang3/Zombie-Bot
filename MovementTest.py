import keyboard
import time

print("Switch to Minecraft window within 5 seconds...")
time.sleep(5)

print("Pressing 'w' key for 2 seconds...")
keyboard.press('w')
time.sleep(2)
keyboard.release('w')
print("Done.")
