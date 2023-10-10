#!/usr/bin/python3
"""Defines the Area and Perimeter of a Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): Te height of the new rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set the width of the Rectangle."""
            return self.__width

        @width.setter
        def width(self, width):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width

        @property
        def height(self):
            """Get/set the height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, width):
            if not isinstance(width, int):
                raise TypeError("height must be an integer")
            if width < 0:
                raise ValueError("height must be >= 0")
            self.__height = width

        def area(self):
            """Return the area of the rectangle"""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width + self.__height) * 2)
