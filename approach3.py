# Imports
import pyclip
import json
import time
import urllib.request
from pbwrap import Pastebin
from cryptography.fernet import Fernet

# Variables
pb = Pastebin("_QSCCGplbifxea1U_TdNQ2pLKfQsGJEd")
pb.authenticate("rosafy",'8rWR#"G"cm=sG6W')
cbdata = open("cbdata.json","r+")
cbdatajson = json.loads(cbdata.read())
oldclip = cbdatajson["content"]
pyclip.copy(oldclip)
lastupdate = cbdatajson["timestamp"]
latestpost = pb.create_paste_from_file("cbdata.json",2,"clipboard","N","json")

# Functions
def clipboard_updated_event(newclip):
    global cbdata
    global oldclip
    global lastupdate
    lastupdate = time.time()
    cbdata.seek(0)
    json.dump({"type":"txt","content":newclip,"timestamp":lastupdate},cbdata, ensure_ascii=False, indent=4)
    print(f"Updated: {newclip} at {lastupdate}")
    oldclip = newclip
    return


# Main Loop
while True:
    try:
        pbdata = json.loads(pb.get_user_raw_paste(latestpost))
    except:
        latestpost = pb.create_paste_from_file("cbdata.json",2,"clipboard","N","json")
        latestpost = latestpost.replace("https://pastebin.com/","")
        pbdata = json.loads(pb.get_user_raw_paste(latestpost))
    cbdata.seek(0)
    cbdatajson = json.loads(cbdata.read())
    if cbdatajson != pbdata:
        if cbdatajson["timestamp"] > pbdata["timestamp"]:
            pb.delete_user_paste(latestpost)
            latestpost = pb.create_paste_from_file("cbdata.json",2,"clipboard","N","json")
        else: 
            json.dump(pbdata,cbdata)
    try:
        newclip = pyclip.paste()
        newclip = newclip.decode()
        if newclip != oldclip:
            clipboard_updated_event(newclip)
            oldclip = newclip
    except Exception as e:
        print(f"Clipboard access error: {e}")
    time.sleep(0.1)