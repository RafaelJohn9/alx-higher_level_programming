#!/bin/bash
# a bash script that takes in a URL and displays all HTTP
curl -sIX OPTIONS $1 | grep "Allow:" | cut -d ' ' -f 2-
