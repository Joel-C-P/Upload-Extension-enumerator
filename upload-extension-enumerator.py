#!/usr/bin/env python3 

import signal 
import time 
import sys
import pdb
import requests
import re 

def def_handler(sig, frame):

    print("\n\n[+]Saliendo...")

    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)


#Variabel global

transfer_url = "http://10.129.58.48/transfer.aspx"

def upload_extension():
   
    s = requests.session()
    r = s.get(transfer_url)
    
    param1_viewState = re.findall(r'id="__VIEWSTATE" value="(.*?)"', r.text)[0]
    
    param2_eventValidation = re.findall(r'id="__EVENTVALIDATION" value="(.*?)"', r.text)[0]


    print(param2_eventValidation)

    print(param1_viewState)

    post_data = {
        '__VIEWSTATE': param1_viewState,
        '__EVENTVALIDATION': param2_eventValidation,
        #3re field i'll put it apart because python can handle this format
        'btnUpload': 'Upload'
    }

    #3re feeld
    param3_fileUploaded =  { 'FileUpload1': ('test.txt', 'imangen this sis something like hello workld')}


    r = s.post(transfer_url, data=post_data, files=param3_fileUploaded)

if __name__=='__main__':
    upload_extension()

