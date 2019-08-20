#!/bin/bash
# send a POST request with certain bodies
curl -s -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD' "$@"
