#!/usr/bin/python3
# Author: Muiz Olaore

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return c
    else:
        c = sub(a, b)
        return c