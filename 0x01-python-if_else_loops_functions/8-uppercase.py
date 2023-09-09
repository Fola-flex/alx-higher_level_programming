#!/usr/bin/python3
# Function to print string in uppercase
# Author - Muiz Olaore

def uppercase(str):
    """Print a string in uppercase."""
    output = ""
    for c in str:
        output += c
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
    print("{}".format(output), end="\n")
