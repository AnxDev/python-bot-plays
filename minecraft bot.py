from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np
import win32api, win32con
import pynput
import pydirectinput

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
mouse = pynput.mouse.Controller()
# new world
click(962, 393)
time.sleep(2)
click(1110, 411)
click(1110, 411)
time.sleep(2)
pydirectinput.click(921, 167)
time.sleep(3.2)
# seed
# seed: '6135999453849993090
pydirectinput.write("- 6135999453849993090")
time.sleep(1)
click(1246, 157)
time.sleep(4.5)
click(801, 1003)
click(803, 1004)
# world generation
time.sleep(15)
pydirectinput.keyDown('w')
time.sleep(15)
pydirectinput.keyUp("w")
time.sleep(2)
click2(959, 533)
time.sleep(5)
pydirectinput.keyDown("e")
time.sleep(0.5)
pydirectinput.keyUp("e")
time.sleep(1)
# crafting
pydirectinput.click(808, 657)
time.sleep(0.8)
pydirectinput.click(996, 418)
time.sleep(1)
pydirectinput.click(1106, 437)
time.sleep(1)
pydirectinput.click(808, 657)
time.sleep(1)
pydirectinput.click(808, 657)
time.sleep(2)
pydirectinput.rightClick(996, 418)
time.sleep(1)
pydirectinput.rightClick(1031, 414)
time.sleep(1)
pydirectinput.rightClick(995, 454)
time.sleep(1)
pydirectinput.rightClick(1033, 450)
time.sleep(2)
pydirectinput.click(1106, 437)
time.sleep(1)
pydirectinput.click(808, 657)
#click2(959, 533)-3635737710501644033
