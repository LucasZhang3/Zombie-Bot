
# Minecraft Zombie YOLOv5 Triggerbot 

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)


##  Overview

This project uses a custom-trained YOLOv5 model to detect zombies in Minecraft by capturing the game window in real-time. When zombies are detected within a configurable distance, the bot automatically attacks, simulating player input without modifying the game or using any Minecraft API.

The included GUI lets you adjust the delay between hits (to match weapon cooldowns) and distance threshold for when to attack.

  
##  Requirements

1. Python 3.x

2. PyTorch

3. OpenCV (opencv-python)

4. numpy

5. pygetwindow

6. mss

7. pyautogui

8. keyboard

9. Tkinter (usually included with Python)

10. Windows OS (tested)


```bash
pip install torch torchvision opencv-python numpy pygetwindow mss pyautogui keyboard
```

##  How to Use

1. Run Minecraft in windowed mode, ensure the window title includes “Minecraft”.
2. Verify your YOLOv5 model weights path is set correctly in the script.
3. **Run the script**:
   ```bash
   python MCML.py
   ```
4. Use the GUI sliders to set:

5. Delay between hits (weapon cooldown time)

6. Distance threshold (how close zombies must be to trigger an attack)

7. Click Start to activate the triggerbot.

8. Watch the detection window showing boxes around zombies.

9. Click Stop or close windows to quit.


##  Demo

![2025-06-24 22-51-48](https://github.com/user-attachments/assets/c4b61dc2-52fa-41c6-833b-8b58ab98b3d2)
