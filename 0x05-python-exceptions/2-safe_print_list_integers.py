#!/usr/bin/python3
def safe_print_list_integers(my_list=[], E=0):
    """
    Print the first E elements of a list and only integers.

    :param my_list: List to print.
    :param E: Number of elements to print.
    :return: Number of elements printed.
    """
    count = 0
    for i in range(E):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1

        except (ValueError, TypeError):
            continue

    print("")
    return (count)
