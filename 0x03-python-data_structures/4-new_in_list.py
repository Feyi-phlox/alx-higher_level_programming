#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list

        my_list[:] = copy_list
        copy_list[idx] = element
        return copy_list
