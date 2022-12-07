#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_res = set(my_list)
    res = 0
    for i in set_res:
        res += i
    return res
