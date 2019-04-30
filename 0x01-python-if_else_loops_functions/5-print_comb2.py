#!/usr/bin/python3
for first in '0123456789':
    for second in '0123456789':
        print('{}{}'.format(first, second), end='')
        if first != '9' or second != '9':
            print(', ', end='')
print()
