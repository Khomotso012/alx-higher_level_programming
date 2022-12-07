#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_res = set(my_list)
    list_res = (list(set_res))
    return sum(list_res) 
