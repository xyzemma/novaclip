# Imports
import pyclip
import json
import time
import urllib.request
from pbwrap import Pastebin

# Variables
pbfile = open("pbdata.json")
pb = Pastebin("_QSCCGplbifxea1U_TdNQ2pLKfQsGJEd")
pb.authenticate("rosafy",'8rWR#"G"cm=sG6W')
latestpost = pb.create_paste_from_file("cbdata.json",2,"test","N","json")
latestpost = latestpost.replace("https://pastebin.com/","")
print(pb.get_user_raw_paste(latestpost))
pb.delete_user_paste(latestpost)
oldclip = ""
cbdata = open("cbdata.json","r+")
lastupdate = None

# Functions
def clipboard_updated_event(newclip):
    global cbdata
    global oldclip
    global lastupdate
    lastupdate = time.time()
    print(f"Updated: {newclip} at {lastupdate}")
    oldclip = newclip
    return

# Main Loop
while True:
    try:
        newclip = pyclip.paste()
        if newclip != oldclip:
            clipboard_updated_event(newclip)
            oldclip = newclip
    except Exception as e:
        print(f"Clipboard access error: {e}")
    time.sleep(0.1)