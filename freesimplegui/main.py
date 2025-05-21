# Build a basic window with a text element and a button.

import FreeSimpleGUI as sg

# layout defines what is in the window
layout = [
    [sg.Text("Hello, World!")],
    [sg.Button("Click Me")],
    [sg.Text("Enter your name:")],
    [sg.InputText(key="name")],
    [sg.Button("Greet Me")],
]
# window defines attributes about the window
window = sg.Window("My First GUI", layout, size=(400, 400))

# Event loop needed to keep window open and interact
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Click Me":
        print("Button clicked!")
    elif event == "Greet Me":
        name = values["name"]
        print(f"Hello, {name}!")
        continue
    window.close()
