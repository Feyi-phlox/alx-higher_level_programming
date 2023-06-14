#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    total = 0

    for num in my_list:
        total += num
    return total

