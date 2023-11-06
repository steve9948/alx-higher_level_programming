#!/usr/bin/python3

'''A class MyList is a child of list.'''


class MyList(list):
    '''Method to print list in ascending order.'''

    def print_sorted(self):
        '''Sort and return the list.'''

        print(sorted(self))
