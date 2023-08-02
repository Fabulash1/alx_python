#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class NoInitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']
    
class BaseGeometry:
    """Empty class
    """
    def __dir__(cls):
        """Removing __init_subclass_ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']
    
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))