#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes a new rectangle.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height