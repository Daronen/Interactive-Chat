import PySimpleGUI as sg


layout = [
    [sg.Text("Testing"), sg.Input(key="IN-"), sg.FileBrowse()],
    [sg.Text("OUtput folder"), sg.Input(key="-out-"), sg.FileBrowse()],
    [sg.Exit(), sg.Button("Convert to CSV")],
]

window = sg.Window("Test window", layout)


while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert to CSV":
        sg.popup_error("Not yet implemented")
window.close()