#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc_sum = 0
    for index in range(len(sys.argv) - 1):
        argc_sum += int(sys.argv[index + 1])
    print("{}".format(argc_sum))
