#!/bin/bash
# find the size in bytes of a web resource
curl -Is "$@" | grep -Pio '(?<=Content-Length:)\s+\d+' | tr -d ' '
