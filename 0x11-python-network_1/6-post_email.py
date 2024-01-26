#!/usr/bin/python3
""" module doc """

import sys
import requests

if __name__ == '__main__':
    result = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(result.text)
