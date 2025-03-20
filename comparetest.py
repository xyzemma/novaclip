import keyboard
import json
import pyclip
import pyautogui as pya
import time
import base64
clipboard = ""
while True:
    tempclip = pyclip.paste()
    datafile = open("cbdata.json","r+")
    data = json.loads(datafile.read())
    if not data["content"] == tempclip:
        if tempclip == clipboard:
            clipboard = data["content"]
            pyclip.copy(clipboard)
        else:
            data["content"] = tempclip
            clipboard = tempclip
            datafile.truncate(0)
            datafile.seek(0)
            json.dump(data,datafile,indent=4)
    time.sleep(1)