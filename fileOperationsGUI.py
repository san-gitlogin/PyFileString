import PySimpleGUI as fo_gui
from configProcessing import read_config

# ------ GUI ------ #

layout = [

    [fo_gui.Text("Choose Target File:"), fo_gui.Input(key = "-INFILE-"), fo_gui.FileBrowse()],
    [fo_gui.Text("Choose Config File:"), fo_gui.Input(key = "-INCONFIG-"), fo_gui.FileBrowse(file_types=("Config Files", "*.ini*"))],
    [fo_gui.Exit(), fo_gui.Button("Start")]

]

fo_gui.theme('DarkGrey13')
window = fo_gui.Window("FSIF", layout)

while True:
    event, values = window.read()
    print(event,values)

    if event in (fo_gui.WINDOW_CLOSED, "Exit"):
        break
    if event == "Start":
        if values["-INCONFIG-"] and values["-INFILE-"]:
            result = read_config(config_path = values["-INCONFIG-"], file_path = values["-INFILE-"])
            if result:
                fo_gui.popup(f"{result}", title='Result')
        else:
            fo_gui.popup_error("Choose required files !")
window.close()
