#!/usr/bin/python3
# Author: Muiz Olaore

def simple_delete(a_dictionary, key=""):
    if key:
        del a_dictionary[key]
    return a_dictionary