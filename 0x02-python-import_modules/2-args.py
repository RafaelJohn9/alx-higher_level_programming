#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    # Taking command line argument
    arg = sys.argv[1:]
    length = len(arg)
    index = 1
    i = 0

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(index, arg[i]))
    else:
        print("{} arguments:".format(length))
        while length > 0:
            print("{}: {}".format(index, arg[i]))
            i += 1
            index += 1
            length -= 1
