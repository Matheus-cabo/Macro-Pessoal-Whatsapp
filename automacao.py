import pyautogui 
import time 

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("WhatsApp")
pyautogui.press("enter")
time.sleep(4)

pyautogui.click( x=420, y=79)
time.sleep(2)
pyautogui.click( x=455, y=285)







