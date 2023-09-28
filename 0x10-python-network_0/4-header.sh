#!/bin/bash
# a bash script that takes in a url as an arg and sends a GET request to the URL
curl -sX GET -H 'X-School-User-Id: 98' $1
