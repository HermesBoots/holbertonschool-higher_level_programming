#!/bin/bash
# make a request with an extra header
curl -s -H 'X-HolbertonSchool-User-Id: 98' "$@"
