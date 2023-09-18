#!/usr/bin/python3
# Author: Muiz Olaore

def complex_delete(a_dictionary, value):
    dic_keys = list(a_dictionary.keys())

    for dic_value in dic_keys:
        if value == a_dictionary.get(dic_value):
            del (a_dictionary[dic_value])

    return a_dictionary
