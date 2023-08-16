
#!/usr/bin/python3
def uniq_add(my_list=[]):

    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    c = set(my_list)
    result = 0
    for i in c:
        result += i
    return(result)
