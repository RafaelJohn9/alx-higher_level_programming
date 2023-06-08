#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    # prints a sorted list without the files with __
    for name in sorted(dir(hidden_4)):
        if name[:2] == "__":
            continue
        else:
            print("{}".format(name))
