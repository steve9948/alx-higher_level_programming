#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        output = my_list[:]
        output[idx] = element
        return output
    return my_list
