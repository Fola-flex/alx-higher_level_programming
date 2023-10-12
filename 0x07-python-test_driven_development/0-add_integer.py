#!/usr/bin/python3
"""Defines an addition function of integers"""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-foat.
    """
    if (not isinstance(a, int) and not isinstance(a, floats)):
        raise TypeError("a must be on integer")
    if (not isinstance(b, int) and not isinstance(b, floats)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
