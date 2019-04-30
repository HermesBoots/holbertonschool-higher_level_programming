#!/usr/bin/python3
r1 = (122, 96, -2)
r2 = (89, 64, -2)
print(''.join(chr(a)+chr(b) for a, b in zip(range(*r1), range(*r2))), end='')
