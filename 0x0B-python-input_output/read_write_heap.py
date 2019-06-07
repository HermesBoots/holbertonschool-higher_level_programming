#!/usr/bin/python3
"""Change some memory in the heap of a running process

Usage: read_write_heap.py pid search_string replace_string

Args:
    pid: PID of process to hack
    search_string: value to search for in process' heap
    replace_string: value to overwrite search_string with

Returns:
    1 if arguments are incorrect or memory can't be hacked, 0 otherwise

"""


import os
import os.path
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: read_write_heap PID SEARCH_STRING REPLACE_STRING')
        sys.exit(1)
    pid = sys.argv[1]
    search = sys.argv[2]
    replace = sys.argv[3]
    os.chdir(os.path.join('/proc', pid))
    start, end, offset = None, None, None
    with open('maps', 'rt') as maps:
        for line in maps:
            fields = line.split()
            if fields[-1] == '[heap]':
                start, _, end = fields[0].partition('-')
                offset = fields[2]
                break
    if start is None:
        print('Process has no heap')
        sys.exit(1)
    offset = int(offset, 16)
    start = int(start, 16) + offset
    end = int(end, 16)
    print('Heap ranges from {:#x}-{:#x}'.format(start, end))
    with open('mem', 'r+b', buffering=0) as memory:
        memory.seek(start)
        heap = memory.read(end - start)
        address = heap.find(search.encode('ASCII'))
        if address < 0:
            print("Process isn't using that string")
            sys.exit(0)
        print('Target string found at {:#x}'.format(start + address))
        memory.seek(start + address)
        memory.write(replace.encode('ASCII'))
