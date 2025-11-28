#!/usr/bin/python3
"""this is document"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """this is document"""
    def __init__(size,size):
        """this is document""" 
         self.integer_validator("size", size)
         super().__init__(size, size)
         self.__size = size
