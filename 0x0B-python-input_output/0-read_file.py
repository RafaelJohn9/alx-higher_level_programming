#!/usr/bin/python3

"""
read_file: reads  a text UTF8 file and prints it out to the stdout
"""


def read_file(filename=""):
    """
    reads a UTF8 file, if it exists
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
