#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for index in range(len(my_list)):
        print("{:d}".format(my_list[index]))
        #or
        #for index in my_list:
        #print("{:d}".format(index))
