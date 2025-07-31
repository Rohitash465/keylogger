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

How to Set Up the Telegram Bot

Follow these exact steps to create your Telegram bot and connect it with the keylogger.

---

## Step 1: Create Your Telegram Bot

- Open the Telegram app.
- Search for @BotFather and start a chat.
- Send the command:
  /newbot
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



