
import pyperclip
import keyboard
from collections import deque
import time

# Set up a deque to store the last 9 copied items
clipboard_history = deque(maxlen=9)

def add_to_clipboard_history():
    """Adds the current clipboard content to the history."""
    copied_text = pyperclip.paste()
    if copied_text not in clipboard_history:
        clipboard_history.appendleft(copied_text)
    print("Clipboard History:", list(clipboard_history))

# A loop that checks for clipboard changes every second
def monitor_clipboard():
    last_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard:
            add_to_clipboard_history()
            last_clipboard = current_clipboard
        time.sleep(1)  # Poll every second

def setup_hotkeys():
    for i in range(1, 10):
        keyboard.add_hotkey(f'ctrl+l+{i}', lambda idx=i: paste_from_history(idx), suppress=True)

def paste_from_history(index):
    if len(clipboard_history) >= index:
        pyperclip.copy(clipboard_history[index - 1])
        # Simulate Ctrl+V to paste
        keyboard.write(clipboard_history[index - 1])
    else:
        print(f"No item at position {index} in the clipboard history.")

def main():
    setup_hotkeys()
    monitor_clipboard()  # This will run indefinitely

if __name__ == "__main__":
    main()
