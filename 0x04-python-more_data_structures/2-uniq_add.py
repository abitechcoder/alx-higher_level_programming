#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum = 0
    for val in uniq_list:
        sum += val
    return sum
