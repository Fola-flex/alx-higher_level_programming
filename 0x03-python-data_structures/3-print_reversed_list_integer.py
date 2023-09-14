#!/usr/bin/python3
# Author: Muiz Olaore

def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num), end="\n")
