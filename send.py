import sys
import time
import pyautogui  # pip install pyautogui

COUNTDOWN_TIMER = 5

def force_exit():
    print("Usage: python script.py [message_content] [num_messages]")
    exit()

if len(sys.argv) < 3:
    force_exit()

try:
    message_content = sys.argv[1]
    num_messages = int(sys.argv[2])
except ValueError:
    force_exit()

print("Switch to the application or chat window where you want to send messages.")
print(f"Starting in ...")
for i in range(COUNTDOWN_TIMER, 0, -1):
    print(f"{i} ...")
    time.sleep(1)

print("Started sending messages.")

for _ in range(num_messages):
    pyautogui.typewrite(message_content)
    pyautogui.press("enter")
    time.sleep(0.1)

print(f"Done sending {num_messages} messages.")
