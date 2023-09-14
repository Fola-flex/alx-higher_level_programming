#!/usr/bin/python3
# Author: Muiz Olaore

def no_c(my_string):
    list = []
    str = ''
    for i in my_string:
        list.append(i)
        if (i == 'c') or (i == 'C'):
            list.remove(i)
    return str.join(list)
