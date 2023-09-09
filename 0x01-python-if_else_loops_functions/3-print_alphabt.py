#!/usr/bin/python3
#Print the alphabets excets q and e
for letter in range(97, 122):
    if chr(letter) !='q' and chr(letter) !='e':
        print("{}".format(chr(letter), end=""))
