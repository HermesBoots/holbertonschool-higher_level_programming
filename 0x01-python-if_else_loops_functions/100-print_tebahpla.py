#!/usr/bin/python3
print(
    ''.join(
        chr(a) + chr(b) for a, b in zip(
            range(122, 96, -2),
            range(89, 64, -2)
        )
    ),
    end=''
)
