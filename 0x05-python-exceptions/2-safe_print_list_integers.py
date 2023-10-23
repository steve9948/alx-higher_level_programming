#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    """
    Print the first x elements of a list if they are integers.

    :param my_list: List to be printed.
    :param x: Number of elements to access in my_list.
    :return: Number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

