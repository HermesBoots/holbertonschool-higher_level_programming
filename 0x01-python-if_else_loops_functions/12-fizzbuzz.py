#!/usr/bin/python3
def fizzy(number):
    if number % 15 == 0:
        return 'FizzBuzz '
    if number % 5 == 0:
        return 'Buzz '
    if number % 3 == 0:
        return 'Fizz '
    return str(number) + ' '


def fizzbuzz():
    print(''.join(fizzy(i) for i in range(1, 101)), end='')
