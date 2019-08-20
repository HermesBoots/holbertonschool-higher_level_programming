#!/bin/bash
# display the status code of a response using only curl
curl -s -o /dev/null -w '%{http_code}' "$@"
