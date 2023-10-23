#!/usr/bin/python3
'''A function that prints the first x elements of a list and only intagers'''
def safe_print_list_integers(my_list=[], x=0):
      try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True

