#!/usr/bin/python3
def list_division(list_1, list_2, list_length):
    """
    Divides element by element 2 lists.

    :param my_list_1: First List.
    :param my_list_2: Secend List.
    :list_length: Lenght of the  long list.
    :return: The new list.
    """
    nw_list = []
    for i in range(list_length):
        try:
            div = list_1[i] / list_2[i]

        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            nw_list.append(div)
    return (nw_list)
