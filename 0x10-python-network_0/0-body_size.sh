#!/usr/bin/env bash
# this script exctracts the content length in bits of the html document passed in curl

url=$1
curl -s $url | wc -c
