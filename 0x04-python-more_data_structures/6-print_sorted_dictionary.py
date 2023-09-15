#!/usr/bin/python3
# Author: Muiz Olaore

def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for i in sorted_dic:
        print("{}: {}".format(i, a_dictionary[i]), end="\n")
