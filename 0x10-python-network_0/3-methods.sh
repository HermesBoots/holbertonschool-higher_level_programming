#!/bin/bash
# list the methods allowed on a remote resource
curl -Is "$@" | grep -i Allow: | cut -d ' ' -f 2-
