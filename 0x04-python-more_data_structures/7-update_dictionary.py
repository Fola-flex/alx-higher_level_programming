#!/usr/bin/python3
# Author: Muiz Olaore

def update_dictionary(a_dictionary, key, value):
    sorted_dic = sorted(a_dictionary)
    for i in sorted_dic:
        if i == key:
            a_dictionary[i] = value
        else:
            a_dictionary[key] = value
        print("{}: {}".format(i, a_dictionary[i]), end="\n")

