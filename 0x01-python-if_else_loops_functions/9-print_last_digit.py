#!/usr/bin/python3
#Function to print last digit of a number
#Author: Muiz Olaore

def print_last_digit(number):
    print("{}".format(abs(number) % 10), end="")
