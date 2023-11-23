#!/usr/bin/python3

def add_integer(a, b=98):
    """Return the integer addition of a and b.
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a is an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b is an integer")
    return (int(a) + int(b))
