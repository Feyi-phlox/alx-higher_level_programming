#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in my_list[:x]:
        try:
            print("{:d}".format(index), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        print()
        return count
