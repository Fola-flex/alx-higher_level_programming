#!/usr/bin/python3
# Author: Muiz Olaore

def element_at(my_list, idx):
    if (idx > 0) or (idx < len(my_list) - 1):
        print("Element at index {:d} is {}".format(idx, my_list[idx]), end='')
    else:
        return None
