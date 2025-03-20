import keyboard
import json
import pyclip
import pyautogui as pya
import time
import base64
import os
from pathlib import Path
clipboard = ""
while True:
    datafile = open("cbdata.json","r+")
    tempclip = pyclip.paste()
    data = json.loads(datafile.read())
    if data["type"] == "txt":
        tc = tempclip.decode("utf-8")
    else:
        tc = base64.b64encode(tempclip).decode("utf-8")
    if not data["content"] == tc and not data["contentb64"] == tc:
        if tempclip == clipboard:
            print("a")
            if data["type"] == "txt":
                clipboard = data["content"]
                pyclip.copy(clipboard)
            else:
                clipboard = data["contentb64"]
                pyclip.copy(base64.b64decode(clipboard.encode()))
        else:
            print("b")
            try:
                clipdecoded = tempclip.decode("utf-8")
            except:
                data["contentb64"] = base64.b64encode(tempclip).decode("utf-8")
            else:
                if "file://" in clipdecoded:
                    testclipdecoded = clipdecoded.replace("file://","")
                    testclipdecoded = testclipdecoded.replace("\u0000","")
                    if Path(testclipdecoded).exists():
                        with open(testclipdecoded,"rb") as tcdc:
                            encoded = base64.b64encode(tcdc.read())
                            data["content"] = clipdecoded
                            data["contentb64"] = encoded.decode("utf-8")
                            data["type"] = "bin"
                            tcdc.close()
                    else:
                        data["content"] = clipdecoded
                        data["type"] = "txt"
                        data["contentb64"] = ""
                else:
                        data["content"] = clipdecoded
                        data["type"] = "txt"
                        data["contentb64"] = ""
            clipboard = tempclip
            datafile.truncate(0)
            datafile.seek(0)
            json.dump(data,datafile,indent=4)
    time.sleep(1)