import time
import ctypes
from psutil import process_iter

# Function to show a notification on Windows
def show_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

# Function to check for new "streamreader" processes
def check_new_streamreader():
    # Get the list of all running processes
    processes = process_iter(['name'])

    # Loop through each process and check if it is a "streamreader" process
    for p in processes:
        if "streamreader" in p.info['name']:
            show_notification("Process Alert", "New possible reverse shell process created")
            break

# Continuous loop to check every 10 seconds
while True:
    # Wait for 10 seconds before checking again
    time.sleep(10)
    check_new_streamreader()
