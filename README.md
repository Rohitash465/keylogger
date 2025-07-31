# Telegram-Based Keylogger (Python)

A Python keylogger that runs silently in the background, captures keystrokes, and sends them to a Telegram bot when the **Enter** key is pressed. Built for educational use in ethical hacking labs and cybersecurity training.

---

## ⚠️ Legal & Ethical Disclaimer

> This tool is created strictly for educational and research purposes.  
> Unauthorized use against other people or systems is illegal.  
> Use it only on your own machines or in controlled environments with permission.

---

## Features

- Stealth background execution (daemon)
- Sends keystrokes to Telegram only on `Enter`
- Handles `backspace`, `space`, and visible characters
- Real-time key delivery to your Telegram chat
- Clean and simple setup using Python

---

## Requirements

Install required Python packages:

```bash
pip install pynput requests
```

# How to Set Up the Telegram Bot

Follow these exact steps to create your Telegram bot and connect it with the keylogger.

---

## Step 1: Create Your Telegram Bot

- Open the Telegram app.
- Search for @BotFather and start a chat.
- Send the command:
  ```/newbot```
- BotFather will ask you for:
    - A name → any name you want (e.g., KeyLogger Bot)
    - A username → must end in bot (e.g., loggerx_bot)
- After successful creation, you’ll get your bot token like:
  ```
  123456789:ABCdefGhIJKlmNoPQrstUvWXyz
  ```

  ---

## Step 2: Start Your Bot

- In Telegram, search for your newly created bot (@loggerx_bot).
- Click Start or type any message like Hello.

This is necessary so Telegram can register your chat for updates.

---

##  Step 3: Get Your Chat ID

- Open your browser and go to:
  ```
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
  ```
  Replace <YOUR_BOT_TOKEN> with the actual token from BotFather.
- In the response, find a block like:
  ```json
  "chat": {
  "id": 200535565,
  ...
  }
  ```
-  Copy the number inside id → this is your CHAT_ID

---

# How to Use

Edit the following lines in your keylogger.py file:

```python
BOT_TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'
```

---

# Respect the Hacker Ethic

> Hack to learn.
> Never hack to harm.
> Always ask permission before testing others' systems.

  
