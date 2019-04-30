#!/usr/bin/python3
index = 25
for little, big in zip(range(122, 96, -1), range(90, 64, -1)):
    print('{:c}'.format(little if index % 2 else big), end='')
    index -= 1
