#!/usr/bin/python3
def safe_print_list(my_list=[], E=0):
    """
    Print SAFTLEY E elements of a list, if E > len(list), print until the end
    of the list.

    :param my_list: List to print.
    :param E: Number of elements to print.
    :return: The number of the elements printed.
    """
    try:
        count = 0
        for i in range(E):
            print(my_list[i], end="")
            count += 1

    except IndexError:
        pass

    print()
    return (count)
