import keyboard
import json
import pyclip
import pyautogui as pya
import time
import base64
while True:
    datafile = open("cbdata.json","r+")
    data = json.loads(datafile.read())
    datafile.truncate(0)
    datafile.seek(0)
    json.dump(data,datafile,indent=4)