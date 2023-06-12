#!/usr/bin/python3
def no_c(my_string):
    new_str = ['c', 'C']
    for items in my_string:
        if items in my_string:
            my_string.remove(items)
    return my_string
