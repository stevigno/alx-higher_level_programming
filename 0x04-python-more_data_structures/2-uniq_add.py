
#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = set(my_list)
    rlt = 0
    for i in c:
        rlt += i
    return(rlt)
