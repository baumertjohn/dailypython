# Build a basic window with a text element and a button.

import FreeSimpleGUI as sg

layout = [[sg.Text("Hello, World!"), sg.Button("Click Me")]]
window = sg.Window("My First Gui", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Click Me":
        print("Button clicked!")
    window.close()
