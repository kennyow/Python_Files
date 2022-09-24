import pyautogui, pyperclip
from time import sleep

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=360, y=364, clicks=2)