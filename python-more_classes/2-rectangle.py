#!/usr/bin/python3
"""This is documentation of the class."""


class Rectangle:
    """This is a Square class."""

    def __init__(self, width=0, height=0):
        """Initialize the square with optional size."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return arena"""
        return self.__width * self.__height 
    
    def perimeter(self):
        """Return perimetr"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
