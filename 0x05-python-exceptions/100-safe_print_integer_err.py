#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error:
        print("Exception: " + error.args[0], file=stderr)
        return False
    else:
        return True
