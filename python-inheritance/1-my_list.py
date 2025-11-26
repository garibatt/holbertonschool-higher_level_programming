#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list.
"""


class MyList(list):
    """
    Represents a list that can be printed in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
