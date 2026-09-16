#!/usr/bin/env python3 

import signal 
import time 
import sys
import pdb
import requests
import re
from pwn import *



def def_handler(sig, frame):

    print("\n\n[+]Saliendo...")

    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)


#Variabel global

transfer_url = "http://IpTargetHere/SiteThatRequereUploadAFile"
#burp = {"http": "http://127.0.0.1:3439"}


def extension_dicctionary():

    f = open("/usr/share/seclists/Discovery/Web-Content//raft-medium-extensions-lowercase.txt", "rb")
    
    p1 = log.progress("Upload-Extension-Enumerator")
    p1.status("Scanning valid extensions....")

    time.sleep(1.5)

    
    for extension in f.readlines():
        extension = extension.decode().strip()
        p1.status(f"Probando con la extension {extension}")
        upload_extension(extension)

def upload_extension(extension):
   
    s = requests.session()
    r = s.get(transfer_url)
    
    param1_viewState = re.findall(r'id="__VIEWSTATE" value="(.*?)"', r.text)[0]
    
    param2_eventValidation = re.findall(r'id="__EVENTVALIDATION" value="(.*?)"', r.text)[0]




    post_data = {
        '__VIEWSTATE': param1_viewState,
        '__EVENTVALIDATION': param2_eventValidation,
        #3re field i'll put it apart because python can handle this format
        'btnUpload': 'Upload'
        }

    #3re feeld
    param3_fileUploaded =  {'FileUpload1': ('test%s' % extension, 'imangen this sis something like hello workld')}


    r = s.post(transfer_url, data=post_data, files=param3_fileUploaded)

    if "Invalid File. Please try again" not in r.text: 
        log.info(f"La extencion es correcta {extension}")

def main():
    extension = extension_dicctionary()
    upload_extension(extension)

if __name__=='__main__':


    main()
