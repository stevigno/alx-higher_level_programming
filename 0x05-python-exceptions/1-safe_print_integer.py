#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print a value using "{:d}".format

    :param value: Value to print
    :return: True if the value is an integer, False if not.
    """
    try:
        print("{:d}".format(value))
        return (True)

    except (ValueError, TypeError):
        return (False)
