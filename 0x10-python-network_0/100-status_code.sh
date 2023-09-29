#!/bin/bash
# bash script that sends a request to a URL passed as arg
curl -so /dev/null -w %{http_code} $1
