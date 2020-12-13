from sys import executable
import sys
from subprocess import Popen, CREATE_NEW_CONSOLE
import numpy as np
import cv2
import webbrowser
from mss import mss
from PIL import Image, ImageChops
import PIL
from time import sleep

import pyautogui

f = open("zoomLinks.txt", "r",encoding="utf-8")
i=0
for string in f:
    print(f"{i+1} : {string.split(';')[0]}")
    i=i+1
f.close()
text = input('Skriv siffra för vilken länk du vill följa:')
row = int(text)-1
if row<0 or row>=i:
    print('Invalid number')
    exit()

f = open("zoomLinks.txt", "r")
info = []; i=0
for string in f:
    if i==row:
        info = string.split(';')
        break
    i=i+1
f.close()



f = open("settings.txt", "r",encoding="utf-8")
top = 0; left = 0; width = 0; height = 0; i=0
clickx = 0; clicky = 0

for row in f:
    setting = row.split(';')[0]
    val     = row.split(';')[1]
    if setting == 'left':
        left = int(val)
    elif setting == 'right':
        width = abs(left-int(val))
    elif setting == 'top':
        top = int(val)
    elif setting == 'bottom':
        height = abs(left-int(val))
    elif setting == 'click x':
        clickx = int(val) 
    elif setting == 'click y':
        clicky = int(val)
    i=i+1
f.close()
mon = {'top': top, 'left': left, 'width': width, 'height': height}

sct = mss()
zoom = Image.open("pictures/zoom.png")
targ = ImageChops.difference(zoom, zoom)
webbrowser.open(info[1])
password = info[2]
delay = 0.3

while 1:
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    diff = ImageChops.difference(zoom, img)
    if list(targ.getdata()) == list(diff.getdata()):
        sleep(delay)
        pyautogui.hotkey("altleft", "tab")
        sleep(delay)
        pyautogui.hotkey("ctrlleft", "w")
        sleep(delay)
        pyautogui.hotkey("altleft", "tab")
        sleep(delay)
        pyautogui.click(clickx, clicky)
        for c in password:
            pyautogui.typewrite([c]) 
        pyautogui.typewrite(["enter"]) 
            
        cv2.destroyAllWindows()
        exit()
    cv2.imshow('test', np.array(diff))
    cv2.moveWindow('test', 20, 20)
    if password == 'x\n':
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break