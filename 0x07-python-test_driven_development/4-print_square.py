#!/usr/bin/python3
def print_square(size):
    """ prints square of # shape.

        Args:
            size: side lenght
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
     # Check that size is an int
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for count in range(size):
        for item in range(size):
            print('#', end='')
        print()
