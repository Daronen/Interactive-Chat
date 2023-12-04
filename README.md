# InteractiveChat

This project is built upon github.com/DougDougGithub/TwitchPlays.
These are the python files that allows Twitch Chat to control your keyboard or mouse to play a game.

To run the program execute the `gui.py` by passing it as an argument to `python` executable in the command line, e.g. `python gui.py`.
It will open up the gui window which would allow you to use the program. 

For the program to execute/run without any error.

Make sure you have `Python 3.9` or later version installed on your device.  
Additionally, you will need to install the following python modules using `pip`:  
```
python -m pip install keyboard  
python -m pip install pydirectinput  
python -m pip install pyautogui  
python -m pip install pynput  
python -m pip install requests  

python -m pip install pysimplegui
```

Once Python is set up, simply change the Twitch username in `TwitchPlays_TEMPLATE.py`, and you'll be ready to go.


#### Credits
This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated for the Youtube side. For now I am not reviewing any pull requests or code changes, this code is meant to be a simple prototype that is uploaded for educational purposes. But feel free to fork the project and create your own version!
