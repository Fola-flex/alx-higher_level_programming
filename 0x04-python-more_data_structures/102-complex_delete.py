#!/usr/bin/python3
# Author: Muiz Olaore

def complex_delete(a_dictionary, value):
    for key, dic_value in a_dictionary.items():
        if dic_value == value:
            del (a_dictionary[key])
        return a_dictionary

    return a_dictionary
