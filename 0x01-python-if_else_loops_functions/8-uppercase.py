#!/usr/bin/python3
def toupper(char):
    return chr(ord(char) - 32) if char >= 'a' and char <= 'z' else char


def uppercase(str):
    print(''.join(toupper(c) for c in str))
