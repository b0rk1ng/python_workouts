"""
Transform a hex number into an integer."
"""

import sys

def hex_output(hexnum):
    """
    Turn hex into int
    """
    decnum = 0
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

if __name__ == "__main__":
    hex_output(sys.argv[1])










