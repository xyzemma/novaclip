import keyboard
import pyclip
import pyautogui as pya
import time
import base64
while True:
    if keyboard.is_pressed("ctrl+alt+c"):
        while True:
            if not keyboard.is_pressed("ctrl+alt+c"):
                break
        pya.hotkey('ctrl', 'c')
        time.sleep(2)
        print(pyclip.paste())
        break