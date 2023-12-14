#!/usr/bin/python3
'''Function that reads a text file (UTF8) encoding and prints it to stdout.'''


def read_file(filename=""):
    '''Opens and reads file using with statement.'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
