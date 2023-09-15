#!/usr/bin/python3
# Author: Muiz Olaore

def only_diff_elements(set_1, set_2):
    return sorted(list(set_1 ^ set_2))
