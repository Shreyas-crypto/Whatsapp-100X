import pyautogui
import time 
time.sleep(2)
count=0
while count<=100:
    pyautogui.typewrite("All is well..")
    pyautogui.press("enter")
    count=count+1