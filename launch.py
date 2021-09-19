from sys import executable
import numpy as np
import cv2
import webbrowser
from mss import mss
from PIL import Image, ImageChops
from time import sleep
import pyautogui

def get_settings():
    f = open("settings.txt", "r",encoding="utf-8")
    i = 0

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
    win_area = {'top': top, 'left': left, 'width': width, 'height': height}
    box_pos = (clickx, clicky)
    return win_area, box_pos

def get_info():
    f = open("zoomLinks.txt", "r",encoding="utf-8")
    strings = []
    for string in f:
        strings.append(string)
    f.close()
    n = len(strings[:])
    [print(i+1,":",strings[i].split(";")[0]) for i in range(n)]

    text = input('Skriv siffra för vilken länk du vill följa:')
    row = int(text)-1
    if row<0 or row>=n:
        print('Invalid number')
        exit()
    if strings[-2:-1] == "\n":
        return (strings[row].split()[0]).split(";")
    return strings[row].split(";")

def open_link(link):
    webbrowser.open(link)

def find_window_on_screen(targ, zoom, win_area):
    screen_pixels = mss()
    while 1:
        screen_pixels.get_pixels(win_area)
        img = Image.frombytes('RGB', (screen_pixels.width, screen_pixels.height), screen_pixels.image)
        diff = ImageChops.difference(zoom, img)
        if list(targ.getdata()) == list(diff.getdata()):
            return True
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        cv2.imshow('test', np.array(diff))
        cv2.moveWindow('test', 20, 20)
        
def enter_info(password, box_pos):
    delay = 0.3
    pyautogui.hotkey("altleft", "tab")
    sleep(delay)
    pyautogui.hotkey("ctrlleft", "w")
    sleep(delay)
    pyautogui.hotkey("altleft", "tab")
    sleep(delay)
    pyautogui.click(box_pos)
    for c in password:
        pyautogui.typewrite([c]) 
    pyautogui.typewrite(["enter"]) 

    cv2.destroyAllWindows()
    return

def main():
    info = get_info()
    win_area, box_pos = get_settings()
    zoom = Image.open("pictures/zoom.png")
    targ = ImageChops.difference(zoom, zoom)
    open_link(info[1])
    password = info[2]
    if password == "x\n":
        cv2.destroyAllWindows()
        return
    if find_window_on_screen(targ, zoom, win_area):
        enter_info(password, box_pos)

if __name__ == "__main__":
    main()
