#!/usr/bin/python3

if __name__ == "__main__":
    # import sys to get cmdline arguments
    import sys
    arg = sys.argv[1:]

    # summation
    sum_1 = 0
    length = len(arg)
    i = 0
    while length:
        sum_1 += int(arg[i])
        i += 1
        length -= 1
    print("{:d}".format(sum_1))
