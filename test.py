from importlib import import_module
import time
import threading


#print(sys.path[0]+ "\Scripts")
#print("C:\Users\lukez\Downloads\447InteractiveChat-main\447InteractiveChat-main\Scripts")
#os.chdir(sys.path[0] + "\Scripts")

#print(os.listdir())

fname = "reverseKeyPressRun"

module = import_module("TwitchPlays_Scripts")
args = [5]

command = threading.Thread(name = 'command', target = module.exec("%s", fname) , args=args)
command.start()
