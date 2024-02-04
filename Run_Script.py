from importlib import import_module
import time
import threading
import os


#print(sys.path[0]+ "\Scripts")
#print("C:\Users\lukez\Downloads\447InteractiveChat-main\447InteractiveChat-main\Scripts")
#os.chdir(sys.path[0] + "\Scripts")

#print(os.listdir())
def run_script(module_name, fname, args):
    #os.chdir(os.path.dirname(os.path.abspath(__file__)))
    module = import_module(module_name)
    funct = getattr(module, fname)

    command = threading.Thread(name = 'command', target = funct , args=args)
    command.start()


#run_script("TwitchPlays_Scripts", "reverseKeyPressRun", [5])

"""
def handle_message(message, command_data):

    msg = message
    #username = message['username'].lower()

    print("Got this message from " + "username" + ": " + msg)
    commands = command_data
    # Now that you have a chat message, this is where you add your game logic.
    # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
    # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
    # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
    # Use the pydirectinput library to press or move the mouse

    command = commands[msg]
    for keypresses in command:
        if(keypresses == "HR"):
            for key in command[keypresses]:
                HoldAndReleaseKey(globals()[key], .3)

        if(keypresses == "R"):
            for key in command[keypresses]:
                print("release:", key)
                ReleaseKey(globals()[key])

        if(keypresses == "H"):
            for key in command[keypresses]:
                print("hold:", key)
                HoldKey(globals()[key])

        if(keypresses == "script"):
            print("check")
            module_name = command[keypresses]["fileName"]
            fname = command[keypresses]["functionName"]
            args = command[keypresses]["args"]

            module = import_module(module_name)
            funct = getattr(module, fname)

            command = threading.Thread(name = 'command', target = funct , args=args)
            command.start()






commands = {
    "up": {"HR": [{"key": 'W', "time": 1}, {"key": 'T', "time": 1}]},
    "down": {"HR": [{"key": 'S', "time": 1}]},
    "left": {"HR": ['A']},
    "right": {"HR": ['D']},
    "shoot up": {"R": ['DOWN_ARROW'], "H": ['UP_ARROW']},
    "shoot down": {"R": ['UP_ARROW'], "H": ['DOWN_ARROW']},
    "shoot left": {"R": ['RIGHT_ARROW'], "H": ['LEFT_ARROW']},
    "shoot right": {"R": ['LEFT_ARROW'], "H": ['RIGHT_ARROW']},
    "be a man": {"R": ['UP_ARROW, DOWN_ARROW', 'LEFT_ARROW, RIGHT_ARROW']},
    "reverse": {"script": {"fileName": "TwitchPlays_Scripts", "functionName": "reverseKeyPressRun", "args": [5]}}
}
        


handle_message("reverse", commands)
"""


"""
module_name = "TwitchPlays_Scripts"

fname = "reverseKeyPressRun"

module = import_module(module_name)
args = [5]
funct = getattr(module, fname)

command = threading.Thread(name = 'command', target = funct , args=args)
command.start()

"""