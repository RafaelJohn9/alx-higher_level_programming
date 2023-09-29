#!/usr/bin/python3
"""
solves the highest peak problem
"""


def find_peak(list_of_integers):
    """
   the function calculating the highest peak
   """
   if not list_of_integers:
       return None

   left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak may be in the left half, including mid
            right = mid
        else:
            # Peak may be in the right half, excluding mid
            left = mid + 1

    return list_of_integers[left]
