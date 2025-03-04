# WhatsApp Message Bomber

## Description
This script automates the process of sending multiple messages to a WhatsApp contact using the WhatsApp Desktop application. It opens WhatsApp, searches for the specified contact, and repeatedly sends a predefined message.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- `pyautogui` module (`pip install pyautogui`)
- `keyboard` module (`pip install keyboard`)

## Installation
1. Clone or download this script to your local system.
2. Install the required Python modules if not already installed:
   ```sh
   pip install pyautogui keyboard
   ```

## Usage
1. Open the script in a text editor and modify the following variables:
   - `contact_name`: Set it to the name of the WhatsApp contact.
   - `message`: Define the message you want to send.
   - `count`: Specify the number of times the message should be sent.
2. Run the script:
   ```sh
   python script_name.py
   ```

## Features
- Automatically opens WhatsApp Desktop.
- Searches for a specified contact.
- Sends multiple messages in an automated loop.

## Notes
- The script assumes that WhatsApp Desktop is installed and accessible via the Windows Apps folder.
- You may need to adjust the delay timings (`time.sleep(x)`) if the script runs too fast or too slow.
- Ensure your screen resolution and UI scale do not affect the cursor clicks.

## Disclaimer
This script is intended for educational purposes only. Spamming messages without consent can violate platform policies and may lead to account restrictions. Use responsibly.
