#!/usr/bin/env python3

"""
a script that adds items in a json file
"""


import sys
from typing import List
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items_to_list(items: List[str]) -> List[str]:
    """
    a function that adds item to a list
    """

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    updated_items = existing_items + items
    save_to_json_file(updated_items, "add_item.json")

    return updated_items


if __name__ == "__main__":
    items_to_add = sys.argv[1:]
    updated_list = add_items_to_list(items_to_add)
