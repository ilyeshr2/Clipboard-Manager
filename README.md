
# Clipboard Manager

This Python-based Clipboard Manager allows you to store the last 9 copied items and paste them using custom shortcuts like `Ctrl+L+1` for the last copy, `Ctrl+L+2` for the second last copy, and so on up to `Ctrl+L+9`.


![screen-capture71-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/ed9ddadb-6400-4420-a71c-72a1b9b33fa7)




## Features

- **Clipboard History**: Stores up to the last 9 copied items.
- **Custom Shortcuts**: Paste from history using `Ctrl+L+1`, `Ctrl+L+2`, ..., `Ctrl+L+9`.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Automatic Startup**: Can be configured to run automatically on system startup.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ilyeshr2/clipboard-manager.git
   cd clipboard-manager
   ```

2. Set up a virtual environment:

    ```bash
    py -3 -m venv .venv
    .venv\Scripts\activate
    ```

    
3. **Install the Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Program**:
   ```bash
   python clipboard_manager.py
   ```

5. **Optional: Set Up for Automatic Startup**:
   Follow the instructions below to set the program to run automatically when you start your system.

## Automatic Startup Setup

### Windows

1. Create a shortcut of the `clipboard_manager.py` file.
2. Move the shortcut to the Startup folder (`Win + R` -> `shell:startup`).
3. (Optional) Convert the Python script to an executable using `PyInstaller`.

### macOS

1. Create a `.plist` file in `~/Library/LaunchAgents/`:
   ```bash
   nano ~/Library/LaunchAgents/com.clipboardmanager.plist
   ```
2. Add the following content (replace with your actual script path):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.clipboardmanager</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/path/to/clipboard_manager.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
   </dict>
   </plist>
   ```
3. Save and load the `.plist` file:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.clipboardmanager.plist
   ```

### Linux

1. Create a `.desktop` file in `~/.config/autostart/`:
   ```bash
   nano ~/.config/autostart/clipboard_manager.desktop
   ```
2. Add the following content:
   ```ini
   [Desktop Entry]
   Type=Application
   Exec=python3 /path/to/clipboard_manager.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=Clipboard Manager
   Comment=Start Clipboard Manager on startup
   ```

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions that improve the functionality or expand the feature set are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by the need for better clipboard management in daily workflows.
- Thanks to the authors of the `pyperclip` and `keyboard` libraries for making this project possible.
