#!/usr/bin/python3
"""
find_peak: Finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """def doc"""
    if list_of_integers:
        left = 0
        right = len(list_of_integers) - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return list_of_integers[left]
