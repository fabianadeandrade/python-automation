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

tablecreated = pandas.read_csv("produtos.csv")
print(tablecreated)

# step four: register product
for line in tablecreated.index:
    # codigo
    pyautogui.click(x=-1008, y=270)
    codigo = str(tablecreated.loc[line, "codigo"])
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(tablecreated.loc[line, "marca"])
    pyautogui.write(marca)

    # tipo
    pyautogui.press("tab")
    tipo = str(tablecreated.loc[line, "tipo"])
    pyautogui.write(tipo)

    # categoria
    pyautogui.press("tab")
    categoria = str(tablecreated.loc[line, "categoria"])
    pyautogui.write(categoria)

    # preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tablecreated.loc[line, "preco_unitario"])
    pyautogui.write(preco_unitario)

    # custo
    pyautogui.press("tab")
    custo = str(tablecreated.loc[line, "custo"])
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tablecreated.loc[line, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# step five: Repeat step four until all products are registered
# included command for on stpe four for this step
