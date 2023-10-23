import concurrent.futures
import random
import keyboard
import pydirectinput
import pyautogui
import TwitchPlays_Connection
from TwitchPlays_KeyCodes_DellLaptop import *
#from TwitchPlays_KeyCodes import *


def handle_message(message, command_data):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print("Got this message from " + username + ": " + msg)
        """  
        commands = {
            "up": {"HR": [{"key": W, "time": 1}]}
            "down": {"HR": [{"key": S, "time": 1}]},
            "left": {"HR": [A]},
            "right": {"HR": [D]},
            "shoot up": {"R": [DOWN_ARROW], "H": [UP_ARROW]},
            "shoot down": {"R": [UP_ARROW], "H": [DOWN_ARROW]},
            "shoot left": {"R": [RIGHT_ARROW], "H": [LEFT_ARROW]},
            "shoot right": {"R": [LEFT_ARROW], "H": [RIGHT_ARROW]},
            "be a man": {"R": [UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW]}
        }
        """
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
                    HoldAndReleaseKey(key, .3)

            if (keypresses == "R"):
                for key in command[keypresses]:
                    print("release:", key)
                    ReleaseKey(key)

            if (keypresses == "H"):
                for key in command[keypresses]:
                    print("hold:", key)
                    HoldKey(key)

    except Exception as e:
        print("Encountered exception: " + str(e))




##################### GAME VARIABLES #####################
def TwitchPlaysStart(commands, Twitch_Channel = "exampe", Streaming_on_Twitch = True, Youtube_channel_id = "exampe", Youtube_stream_URL = None,
                     Message_Rate = 0.5, Max_Que_Length = 20, Max_Threads = 100, End_keys = 'shift+backspace'):
    # Replace this with your Twitch username. Must be all lowercase.
    TWITCH_CHANNEL = Twitch_Channel

    # If streaming on Youtube, set this to False
    STREAMING_ON_TWITCH = Streaming_on_Twitch

    # If you're streaming on Youtube, replace this with your Youtube's Channel ID
    # Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
    YOUTUBE_CHANNEL_ID = Youtube_channel_id

    # If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
    # Otherwise you can leave this as "None"
    YOUTUBE_STREAM_URL = Youtube_stream_URL

    ##################### MESSAGE QUEUE VARIABLES #####################

    # MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
    # This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
    # A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch.
    # A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
    # You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
    MESSAGE_RATE = Message_Rate
    # MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages.
    # e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
    # This is helpful for games where too many inputs at once can actually hinder the gameplay.
    # Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
    MAX_QUEUE_LENGTH = Max_Que_Length
    MAX_WORKERS = Max_Threads # Maximum number of threads you can process at a time

    last_time = time.time()
    message_queue = []
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
    active_tasks = []
    pyautogui.FAILSAFE = False

    ##########################################################

    # Count down before starting, so you have time to load up the game
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    if STREAMING_ON_TWITCH:
        t = TwitchPlays_Connection.Twitch()
        t.twitch_connect(TWITCH_CHANNEL)
    else:
        t = TwitchPlays_Connection.YouTube()
        t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)

    while True:

        active_tasks = [t for t in active_tasks if not t.done()]

        #Check for new messages
        new_messages = t.twitch_receive_messages(); #return message in dict format with (msg['username'] msg['message'])
        if new_messages:
            message_queue += new_messages; # New messages are added to the back of the queue
            message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

        messages_to_handle = []
        if not message_queue:
            # No messages in the queue
            last_time = time.time()
        else:
            # Determine how many messages we should handle now
            r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
            n = int(r * len(message_queue))
            if n > 0:
                # Pop the messages we want off the front of the queue
                messages_to_handle = message_queue[0:n]
                del message_queue[0:n]
                last_time = time.time();

        # If user presses Shift+Backspace, automatically end the program
        if keyboard.is_pressed(End_keys):
            exit()

        if not messages_to_handle:
            continue
        else:
            for message in messages_to_handle:
                if len(active_tasks) <= MAX_WORKERS:
                    active_tasks.append(thread_pool.submit(handle_message, message, commands))
                else:
                    print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
 


commands = {
    "up": {"HR": [W]},
    "down": {"HR": [S]},
    "left": {"HR": [A]},
    "right": {"HR": [D]},
    "shoot up": {"R": [J, H, K], "H": [U]},
    "shoot down": {"R": [U, H, K], "H": [J]},
    "shoot left": {"R": [U, J, K], "H": [H]},
    "shoot right": {"R": [U, J, H], "H": [K]},
    "be a man": {"R": [U, J, H, K]}
    }
TwitchPlaysStart(commands, Twitch_Channel = "wizardwolf26", Streaming_on_Twitch = True, End_keys = 'shift+backspace')

