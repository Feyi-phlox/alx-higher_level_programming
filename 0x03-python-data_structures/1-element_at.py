#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx == 0 - idx:
            return None
        elif idx > (len(my_list) - 1):
            return None
        else:
            return my_list[idx]
