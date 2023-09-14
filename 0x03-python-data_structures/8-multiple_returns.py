#!/usr/bin/python3
# Author: Muiz Olaore

def multiple_returns(sentence):
    first_letter = ''
    strength_length = len(sentence)
    if sentence == '':
        first_letter = None
    else:
        first_letter = sentence[0]

    tuple_a = strength_length, first_letter
    return tuple_a
