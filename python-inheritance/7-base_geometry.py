#!/usr/bin/python3
"""This is the BaseGeometry class module."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not int:
            raise TypeError("{} must be integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
        self.name = value
