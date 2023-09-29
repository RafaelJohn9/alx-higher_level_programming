#!/bin/bash
# Bash script that sends json POST Request to url passed as arg
cat $2 | curl -sX POST -H "Content-Type: application/json" -d @- $1
