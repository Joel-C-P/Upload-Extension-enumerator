#!/usr/bin/env python3 

import signal 
import time 
import sys
import pdb
import requests

def def_handler(sig, frame):

    print("\n\n[+]Saliendo...")

    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)


#Variabel global

transfer_url = "http://10.129.58.48/transfer.aspx"

def upload_extension():
    
    r = requests.get(transfer_url)
    
    pdb.set_trace()

if __name__=='__main__':
    upload_extension()

