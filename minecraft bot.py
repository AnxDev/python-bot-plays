from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np
import win32api, win32con

time.sleep(5)

# click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
    time.sleep(0.1) # attende il click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) 
def click2(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
    time.sleep(5) # attende il click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# new world
click(962, 393)
time.sleep(2)
click(1110, 411)

time.sleep(2)
click(921, 167)
time.sleep(0.5)
click(922, 167)
time.sleep(3.2)
# seed
# seed: -3635737710501644033
pyautogui.write("-3635737710501644033")
time.sleep(4)
click(794, 1004)
# world generation
time.sleep(15)
click2(959, 533)
