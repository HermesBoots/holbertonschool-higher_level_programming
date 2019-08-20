#!/bin/bash
# find the size in bytes of a web resource

curl --silent --head "$@" \
| grep --ignore-case --only-matching --perl-regexp '(?<=Content-Length:)\s+\d+' \
| tr --delete ' '
