from pynput import keyboard
import time

kb = keyboard.Controller()

keysHeld = []


def on_press(key):
    global keysHeld
    print('Key: ', key, ' was held')
    if key == keyboard.KeyCode(char ='w'):
        if not("w" in keysHeld):
            print("hold s")
            keysHeld.append("w")
            kb.press('s')
            #HoldKey(S)   

def on_release(key):
    global held
    print('Key: ', key, ' was released')
    if key == keyboard.KeyCode(char ='w'):
        if ("w" in keysHeld):
            keysHeld.remove("w")
            #ReleaseKey(S)
            kb.release('w')

def reverseKeyPress(time_run):
    i=int(time.time()) + time_run
    while(time.time()<=i):
        with keyboard.Listener(suppress=False, on_press=on_press, on_release=on_release) as listener:
            print('listener starts')
            listener.join()

reverseKeyPress(5)