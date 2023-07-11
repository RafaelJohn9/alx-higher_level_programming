#!/usr/bin/python3

"""
write_file:writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ writes in a file or overwrites in an
    existing file
    """

    with open(filename, 'w+', encoding="utf8") as f:
        numberOfCharacters = f.write(text)
    return (numberOfCharacters)
