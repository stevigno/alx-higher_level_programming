#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    set1 = set(my_list)
    lst1 = list(set1)
    numb = 0

    for i in lst1:
        numb = numb + i

    return numb)
