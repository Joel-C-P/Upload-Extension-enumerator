#!/usr/bin/env python3 

import signal 
import time 
import sys
def def_handler(sig, frame):

    print("[+]Saliendo...")

    sys.exit(1);

signal.signal(signal.SIGINT, def_handler)
def upload_extension():
    
    print("hola")

    time.sleep(3)
if __name__=='__main__':
    upload_extension()

