#!/usr/bin/env bash
# this script exctracts the content length in bits of the html document passed in curl

url=$1
content=$(curl -si "$url" | grep -i "Content-Length" | awk '{print $2}')

echo "$content"
