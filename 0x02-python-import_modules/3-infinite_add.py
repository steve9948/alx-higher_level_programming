#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of arguments."""
    import sys

    total = 0
    """Itearete to the final vector"""
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
