#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    argc = len(argv) - 1
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    if argc != 3:
        print('Usage: ' + argv[0] + ' <a> <operator> <b>')
        exit(1)
    a, op, b = argv[1:]
    if len(op) != 1 or op not in ops:
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    a = int(a)
    b = int(b)
    print('{} {} {} = {}'.format(a, op, b, ops[op](a, b)))
