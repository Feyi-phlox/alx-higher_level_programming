#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in my_list[:x]:
            try:
                print("{:d}".format(index), end="")
                count += 1
            except (ValueError, TypeError):
                pass
    except TypeError:
        raise Exception

    print()
    return count
