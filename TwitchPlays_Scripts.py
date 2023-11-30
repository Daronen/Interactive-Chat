import time
import keyboard

def reverseKeyPressRun(time_run):
    keyboard.remap_hotkey("w", "s")
    keyboard.remap_hotkey("s", "w")
    keyboard.remap_hotkey("d", "a")
    keyboard.remap_hotkey("a", "d")
    i=int(time.time()) + time_run
    while(time.time()<=i):
        l=1
        

#def reverseKeyPress(time):
#reverseKeyPressRun(5)
"""
reverseKeyPressRun = threading.Thread(name = 'reverseKeyPressRun', target = reverseKeyPressRun, args=(5,))
reverseKeyPressRun.start()
x=int(time.time()) + 5
while(time.time()<=x):
    print("testing")
reverseKeyPressRun.join()
sys.exit()
"""

#reverseKeyPress(60)
"""
def on_press(key):
    global keysHeld
    print('Key: ', key, ' was held')
    if key == keyboard.KeyCode(char ='w'):
        if not("w" in keysHeld):
            print("hold s")
            keysHeld.append(W)
            HoldKey(S)   

def on_release(key):
    global held
    print('Key: ', key, ' was released')
    if key == keyboard.KeyCode(char ='w'):
        if ("w" in keysHeld):
            keysHeld.remove(W)
            ReleaseKey(S)

def reverseKeyPress(time_run):
    i=int(time.time()) + time_run
    while(time.time()<=i):
        with keyboard.Listener(suppress=True, on_press=on_press, on_release=on_release) as listener:
            print('listener starts')
            listener.join()
"""
