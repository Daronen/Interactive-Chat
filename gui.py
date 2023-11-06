import PySimpleGUI as sg
import TwitchPlays_InteractiveChat as twitchPlays
import InputManager

mappings = {}
Twitch_Channel = ""
Youtube_Channel = ""

large_font = ("Consolas Bold", 21)

sg.theme('DarkGrey13')

"""MAXIMIZE SCREEN"""
MAXIMIZE_SCREEN = False

layout = [
    [sg.Image('interactive_chat_banner_black.png')],
    [sg.Button("Map Buttons to Phrases", key= 'map')],
    [sg.Text("Load Buttons From File"), sg.Input(key="IN-"), sg.FileBrowse()],
    [sg.Button("Load From File", key="Load-")],
    [sg.Button("See Current Mappings", key="View")],
    [sg.Button("Start Program", key= "Start-"), sg.Exit()],
]

if MAXIMIZE_SCREEN:
  window = sg.Window("Interactive Chat", layout, font=large_font, finalize=True)
  window.maximize()
else:
  window = sg.Window("Interactive Chat", layout, font=large_font)



#Opens a new window in order to add new phrase-key pairings to the dictionary
def MapWindow():
  #may want to add more keyboard options
  options = [ "--", "Choose an option",
           "Q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
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
  if MAXIMIZE_SCREEN:
    newWindow = sg.Window("Mapping", layout2, font=large_font, finalize=True)
    newWindow.maximize()
  else:
    newWindow = sg.Window("Mapping", layout2)


  while True:
    event, values = newWindow.read()

    #exit the window
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break

    #add a new key-phrase pair
    if event == "ADD":
      InputManager.addCommand(mappings, values["Phrase-"], "HR", values['Combo-'])
  newWindow.close()


#call python program to start listening to the designated channel's chat
#loads a new window to interact with the user
def startWatching():
  chatLayout = [
    [sg.Text("Enter a channel name then select the Type of Channel")],
    [sg.Text("Channel Name"), sg.Input(key="Channel_Name")],
    [sg.Text("Channel Type:")],
    [sg.Button("Twitch", key="Twitch"), sg.Button("YouTube", key="YouTube"), sg.Button("Both", key="Twitch and Youtube")],
    [sg.Exit()]
  ]

  if MAXIMIZE_SCREEN:
    newWindow = sg.Window("Chat name", chatLayout, font=large_font, finalize=True)
    newWindow.maximize()
  else:
    newWindow = sg.Window("Chat name", chatLayout, font=large_font)

  while True:
    event, values = newWindow.read()

    #Exiting window
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break

    # user chose to stream on twitch
    if event == "Twitch" and values["Channel_Name"] != "":
      newWindow.close()
      twitchPlays.TwitchPlaysStart(mappings, values["Channel_Name"])

    # user chose to stream on youtube
    if event == "YouTube" and values["Channel_Name"] != "":
      sg.popup("Not implemented yet")
      newWindow.close()

    # user chose to stream on twitch and youtube
    if event == "Twitch and Youtube" and values["Channel_Name"] != "":
      sg.popup("Not implemented yet")
      newWindow.close()

  newWindow.close()


while True:
    event, values = window.read()

    #Exiting program
    if event in (sg.WINDOW_CLOSED, "Exit"):
      break
    
    # user chose the map buttons to phrases
    if event == 'map':
      MapWindow()
    
    # user chose to get keybinds from a saved file
    if event == "IN-" or event == "Load-":
      mappings = InputManager.readFile(values["IN-"])

    # user chose to view all current key-phrase mappings
    if event == "View":
      sg.popup(mappings)
    
    # user chose to begin the chat process
    if event == "Start-":
      window.close()
      #########################################add a save file thing here
      startWatching()

window.close()