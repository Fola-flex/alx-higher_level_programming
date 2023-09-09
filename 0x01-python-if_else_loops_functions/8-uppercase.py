#!/usr/bin/python3
# Function to print string in uppercase
# Author - Muiz Olaore

def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
