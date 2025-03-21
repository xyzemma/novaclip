import pyclip
import json
import time
import urllib.request
def clipboard_updated_event(newclip):
    global cbdata
    global oldclip
    global lastupdate
    lastupdate = time.time()
    print(f"Updated: {newclip} at {lastupdate}")
    oldclip = newclip
    return
oldclip = ""
cbdata = open("cbdata.json","r+")
lastupdate = None
while True:
    try:
        newclip = pyclip.paste()
        if newclip != oldclip:
            clipboard_updated_event(newclip)
            oldclip = newclip
    except Exception as e:
        print(f"Clipboard access error: {e}")
    time.sleep(0.1)