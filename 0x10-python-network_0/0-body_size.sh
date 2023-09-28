#!/usr/bin/env bash
# this script exctracts the content length in bits of the html document passed in curl
curl -s $1 | wc -c
