
#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = set(my_list)
    result = 0
    for i in c:
        result += i
    return(result)
