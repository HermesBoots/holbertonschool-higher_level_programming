#!/bin/bash
# send a given JSON request body
curl -s -H 'Content-Type: application/json' -d "@${2}" "$1"
