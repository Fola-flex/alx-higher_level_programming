#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Print a square with the # character

    Args:
        size (int): The height/width of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size is not an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
