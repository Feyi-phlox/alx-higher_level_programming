#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
