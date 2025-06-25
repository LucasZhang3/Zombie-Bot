import pygetwindow as gw

# List all windows
windows = gw.getWindowsWithTitle("Minecraft")

if windows:
    mc_window = windows[0]
    print(f"Title: {mc_window.title}")
    print(f"Position: (left: {mc_window.left}, top: {mc_window.top})")
    print(f"Size: (width: {mc_window.width}, height: {mc_window.height})")
else:
    print("Minecraft window not found. Make sure it's open and not minimized.")
