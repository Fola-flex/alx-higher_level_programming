#!/usr/bin/python3
# Author: Muiz Olaore

def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

        return (max_list - to_sub)


def roman_to_int(roman_string):
    if (type(roman_string) != str) or None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman.keys())

    num = 0
    last_roman_no = 0
    list_num = [0]

    for i in roman_string:
        for r_num in list_keys:
            if r_num == i:
                if roman.get(ch) <= last_roman_number:
                    num += to_subtract(list_num)
                    list_num = [roman.get(i)]
                else:
                    list_num.append(roman.get(i))

                last_roman_no = roman.get(i)

    num += to_subtract(list_num)

    return (num)
