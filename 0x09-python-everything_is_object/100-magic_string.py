#!/usr/bin/python3
def magic_string(s=set((0,))):
    s.add(s.pop() + 1)
    return ', '.join('Holberton' for _ in range(next(iter(s))))
