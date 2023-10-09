#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __ne__(self, other):
        """equal equal method"""
        return super().__eq__(other)

    def __eq__(self, other):
        """not equal method"""
        return super().__ne__(other)
