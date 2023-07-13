#!/usr/bin/python3

"""
append_after: appends file
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends element in a file
    """

    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
