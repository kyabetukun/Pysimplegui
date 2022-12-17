import PySimpleGUI as sg
import requests


sg.theme("Red")
layout = [[sg.Text("牛乳(150円):"),
        sg.Combo(list(range(1,11)), key="-QUANTITY-"),
        sg.Text("個")],
        [sg.Button("購入", key="-SUBMIT-")],
        [sg.Text(key="-AMOUNT-",size=(120,10))]]

window = sg.Window("購入サイト",layout,size=(300,150))

while True:
  event,values = window.read()
  if event == "-SUBMIT-":
    total = 150*int(values["-QUANTITY-"])
    window["-AMOUNT-"].update(value=f"金額は{total}円です。")
    
  if event == sg.WIN_CLOSED:
    break