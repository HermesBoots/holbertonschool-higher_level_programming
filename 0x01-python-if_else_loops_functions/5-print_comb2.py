#!/usr/bin/python3
for first in range(10):
    for second in range(10):
        print('{:d}{:d}'.format(first, second), end='')
        if first != 9 or second != 9:
            print(', ', end='')
print()
