def new_in_list(my_list, idx, new_element):
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = new_element
        return copy
