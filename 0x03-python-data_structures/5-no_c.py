#!/usr/bin/python3
def no_c(my_string):
    new_str = ['c', 'C']
    for items in new_str:
        if item in my_string:
            my_string.remove(item)
    return my_string
