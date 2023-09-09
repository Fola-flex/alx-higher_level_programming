#!/usr/bin/python3
# Function to print string in uppercase
# Author - Muiz Olaore

def uppercase(str):
    output = ""
    """Print a string in uppercase."""
    for i, c in enumerate(str):
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        output += c
    print("{}".format(output), end="\n")
