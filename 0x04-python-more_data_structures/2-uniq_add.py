#!/usr/bin/python3
# Author: Muiz Olaore

def uniq_add(my_list=[]):
    list_set = set(my_list)
    num = 0
    for i in list_set:
        num += i
    return num
