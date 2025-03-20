import keyboard
import json
import pyperclip
import pyautogui as pya
import time
while True:
    datafile = open("cbdata.json","r+")
    data = json.loads(datafile.read())
    