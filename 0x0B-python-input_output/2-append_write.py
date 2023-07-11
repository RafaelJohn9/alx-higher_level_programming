#!/usr/bin/python3

"""
a function that appends a string at the end of  TEXT FILE
"""
def append_write(filename="", text=""):
    """
    appends in a file or creates a new file containning contents
    """
    with open(filename, "a+") as f:
        numberOfCharactersAdded = f.write(text)
    return numberOfCharactersAdded
