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


