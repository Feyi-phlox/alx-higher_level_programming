#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for items in my_string:
        if items != 'c' and items != 'C':
            new_str = new_str + items
    return new_str
