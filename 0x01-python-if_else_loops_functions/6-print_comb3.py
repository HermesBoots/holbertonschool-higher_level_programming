#!/usr/bin/python3
print(', '.join(str(a) + str(b) for a in range(10) for b in range(10) if b > a))
