#!/usr/bin/python3
# Author: Muiz Olaore

def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if idx < 0 or (idx > len(my_list) - 1):
        return my_list
    else:
        del new_list[idx]
        return new_list
