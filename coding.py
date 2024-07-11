import pyautogui
import time

pyautogui.PAUSE = 0.5

# step one - login at the company's login
#  Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# step two: login
pyautogui.click(x=-1110, y=394)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("codesdtest@gmail.com")

pyautogui.press("tab")
pyautogui.write("pass")

pyautogui.click(x=-960, y=540)

time.sleep(3)

# step three: import/export the database
import pandas

table = pandas.read_csv("produtos.csv")
print(table)

# step four: register product
# codigo
pyautogui.click(x=-1008, y=270)
pyautogui.write("codigo")

# marca
pyautogui.press("tab")
pyautogui.write("marca")

# tipo
pyautogui.press("tab")
pyautogui.write("tipo")

# categoria
pyautogui.press("tab")
pyautogui.write("categoria")

# preco_unitario
pyautogui.press("tab")
pyautogui.write("preco_unitario")

# custo
pyautogui.press("tab")
pyautogui.write("custo")

# obs
pyautogui.press("tab")
pyautogui.write("obs")

pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(5000)

