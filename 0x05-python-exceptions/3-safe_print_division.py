#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ret = a / b
    except (TypeError, ZeroDivisionError):
        ret = None
    finally:
        print("Inside result: {}".format(ret))
        return ret
