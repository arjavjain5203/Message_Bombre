import os
import pyautogui
import time

# Open WhatsApp Desktop

os.system("explorer.exe shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")

time.sleep(5)  # Wait for WhatsApp to open

# Contact Name
contact_name = "Enter thr contact name here"

# Message to send
message = "Enter the message here"

# Number of times to send the message
count = 100  

print("Opening search bar using Ctrl + F...")
keyboard.press_and_release('ctrl+f')
time.sleep(2)

# Type Contact Name
print(f"Searching for {contact_name}...")
pyautogui.typewrite(contact_name)
time.sleep(2)  # Increase delay to ensure results load

# Move Cursor to the First Chat and Click 
print("Clicking on the chat...")
pyautogui.click(250, 200)  
time.sleep(2)

# Send Messages
print(f"Sending {count} messages to {contact_name}...")
for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(2)

print("Message bombing completed.")
