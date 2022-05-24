#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

#find files
files = []
for file in os.listdir():
        if file == "voldemort.py" or file == "theKey.key" or file == "harry.py":
                continue
        if os.path.isfile(file):
                files.append(file)

with open("theKey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("enter password \n")
if user_phrase == secretphrase:
    for file in files:
            with open (file, "rb") as thefile:
                    contents = thefile.read()
            contetnt_decrypted = Fernet(secretkey).decrypt(contents)
            with open (file, "wb") as thefile:
                    thefile.write(contetnt_decrypted)
            
    print("decrypted")

else:
    print("try again")