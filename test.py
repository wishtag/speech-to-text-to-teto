import pyautogui
import time

time.sleep(1)
window = pyautogui.getWindowsWithTitle("OpenUtau")[0]
window.activate()
pyautogui.click(window.left + 10, window.top + 10)
time.sleep(1)
window = pyautogui.getWindowsWithTitle("Roblox")[0]
window.activate()
pyautogui.click(window.left + 10, window.top + 10)