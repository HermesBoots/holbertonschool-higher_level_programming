#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        print('{:c}'.format(i - 32 if 97 <= i <= 122 else i), end='')
    print()
