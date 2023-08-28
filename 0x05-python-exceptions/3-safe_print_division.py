#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and print the result.

    :param a: First Number.
    :param b: Seceend Number.
    :return: The value of the division, otherwise: None.
    """
    try:
        result = a / b

    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
