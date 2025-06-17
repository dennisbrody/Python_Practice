
# 🕵️ Python Keylogger (Educational Use Only)

This is a simple Python-based keylogger built using the `pynput` library. It captures keystrokes on the system and logs them to a local file (`key_log.txt`).

> ⚠️ **Disclaimer:** This project is intended for **educational and ethical use only**. Never run or deploy this on machines you do not own or have explicit permission to use.

---

## 📦 Features

- Captures all keystrokes
- Logs to a local text file
- Records special keys like Enter, Shift, Backspace, etc.
- Stops logging when `ESC` is pressed

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-keylogger.git
cd python-keylogger
```

### 2. Install Dependencies

```bash
pip install pynput
```

### 3. Run the Script

```bash
python keylogger.py
```

Once running, the script will:
- Capture all keyboard inputs
- Save them in `key_log.txt` in the same directory
- Stop when `ESC` is pressed

---

## 📁 File Structure

```
python-keylogger/
├── keylogger.py       # Main script
├── key_log.txt        # Log file created at runtime
└── README.md          # Project documentation
```

---

## 🛡️ Important Notes

- This script runs in the foreground unless you modify it for background execution.
- On some systems (like macOS), you may need to allow Accessibility permissions to capture keyboard input.
- Only use this in **lab environments** or for **learning purposes**.

---

## 🧠 Learning Objectives

This project helps reinforce:
- Python scripting basics
- Working with input listeners
- File I/O in Python
- Ethical hacking concepts in a safe, controlled way

---

## ✅ TODO / Possible Enhancements

- [ ] Add timestamps to each keypress
- [ ] Encrypt log file contents
- [ ] Auto-email logs (with Gmail SMTP)
- [ ] Create a simple GUI to toggle logger on/off
- [ ] Package as executable using PyInstaller

---

## 🤝 Author

Created by [Your Name]  
Follow me on GitHub: [github.com/your-username](https://github.com/your-username)
