#!/usr/bin/python3
# Author: Muiz Olaore

def replace_in_list(my_list, idx, element):
    if (idx > 0) or (idx < len(my_list) - 1):
        my_list[idx] = element
        return my_list
    else:
        return my_list
