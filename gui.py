import PySimpleGUI as sg
import TwitchPlays_InteractiveChat
import InputManager

mappings = {}
Twitch_Channel = ""
Youtube_Channel = ""

layout = [
    [sg.Button("Map Buttons to Phrases", key= 'map')],
    [sg.Text("Load Buttons From File"), sg.Input(key="IN-"), sg.FileBrowse()],
    [sg.Button("See Current Mappings", key="View")],
    [sg.Button("Start Program", key= "Start-"), sg.Exit()],
]

window = sg.Window("Interactive Chat", layout)



#Opens a new window in order to add new phrase-key pairings to the dictionary
def MapWindow():
  #may want to add more keyboard options
  options = [ "--", "Choose an option",
           "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
           "a", "s", "d", "f", "g", "h", "j", "k", "l",
           "z", "x", "c", "v", "b", "n", "m"
           ]
  dropdown = sg.Combo(options, key='Combo-')
  layout2 = [
    [[sg.Text("Add")], dropdown],
    [sg.Text("With Phrase"), sg.Input(key="Phrase-")],
    [sg.Button("Add", key= "ADD")],
    [sg.Exit()],
  ]
  newWindow = sg.Window("Mapping", layout2)

  while True:
    event, values = newWindow.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break
    if event == "ADD":
      InputManager.addCommand(mappings, values["Phrase-"], "HR", values['Combo-'])
      #mappings.update({values["Phrase-"]: values['Combo-']} )
      sg.popup(mappings)
  newWindow.close()



#call/run python program to start listening to the designated channel's chat
def startWatching():
  chatLayout = [
    [sg.Text("Enter a channel name then select the Type of Channel")],
    [sg.Text("Channel Name"), sg.Input(key="Channel_Name")],
    [sg.Text("Channel Type:")],
    [sg.Button("Twitch", key="Twitch"), sg.Button("YouTube", key="YouTube"), sg.Button("Both", key="Twitch and Youtube")],
    [sg.Exit()]
  ]
  newWindow = sg.Window("Chat name", chatLayout)

  while True:
    event, values = newWindow.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break
    if event == "Twitch" and values["Channel_Name"] != "":
      TwitchPlays_InteractiveChat.TwitchPlaysStart(mappings, values["Channel_Name"])
      newWindow.close()

    if event == "YouTube" and values["Channel_Name"] != "":
      sg.popup("Not implemented yet")
      newWindow.close()

    if event == "Twitch and Youtube" and values["Channel_Name"] != "":
      sg.popup("Not implemented yet")
      newWindow.close()

  newWindow.close()



while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break
    if event == 'map':
      MapWindow()
    if event == "IN-":
      mappings = InputManager.readFile(values["IN-"])
      InputManager.print_command(mappings)
    if event == "View":
      sg.popup(InputManager.print_command(mappings))
    if event == "Start-":
      startWatching()

window.close()