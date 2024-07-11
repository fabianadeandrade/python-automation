import pyautogui
import time

pyautogui.PAUSE = 0.5

# step one - login at the company's login
#  Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# step two: login
pyautogui.click