#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx == 0 - idx:
            return None
        elif idx > my_list[idx]:
            return None
        else:
            print("{:d}".format(my_list[idx]))
