import pyclip
import json
import time
import urllib.request
def clipboard_updated_event(newclip):
    global oldclip
    print(f"Updated: {newclip}")
    oldclip = newclip
    return
oldclip = ""
while True:
    try:
        newclip = pyclip.paste()
        if newclip != oldclip:
            clipboard_updated_event(newclip)
            oldclip = newclip
    except Exception as e:
        print(f"Clipboard access error: {e}")
    time.sleep(0.1)