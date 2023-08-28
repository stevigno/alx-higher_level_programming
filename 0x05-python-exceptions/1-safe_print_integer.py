#!/usr/bin/python3

def safe_print_list(nw_list=[], E=0):
    """Print E elememts of a list.

    Args:
        nw_list (list): The list to print elements from.
        E (int): The number of elements of nw_list to print.

    Returns:
        The number of elements printed.
    """
    R = 0
    for i in range(E):
        try:
            print("{}".format(nw_list[i]), end="")
            R += 1
        except IndexError:
            break
    print("")
    return (R)
