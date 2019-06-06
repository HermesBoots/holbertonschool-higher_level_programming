#!/usr/bin/python3
"""Monitor a running server log and track statistics about it"""


import signal
import sys


outBuf = []
status = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
    '500': 0
}
total = 0


def signalHandler(sigNum, frame):
    """Handle the signal sent by Ctrl+C

    Args:
        sigNum (int): alway signal.SIGINT
        frame: ignored

    """

    createRecord()


def printStats():
    """Print total size transferred and status code statistics from log"""

    while len(outBuf) > 0:
        print(outBuf.pop())


def createRecord():
    """Format record to be printed"""

    outBuf.append(
        'File size: ' + str(total) + '\n' +
        ('\n'.join(
            k + ': ' + str(v) for k, v in sorted(status.items()) if v > 0
        ))
    )


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signalHandler)
    count = 0
    for line in sys.stdin:
        line, _, size = line.rpartition(' ')
        line, _, code = line.rpartition(' ')
        total += int(size)
        if code in status:
            status[code] += 1
        count += 1
        if count == 10:
            count = 0
            createRecord()
            printStats()
