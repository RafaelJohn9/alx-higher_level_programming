#!/usr/bin/python3

"""
a python script that takes in a url sends a request to the url and
displays teh url and displays the value of the variable X-Requestid
in the response header
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    data = requests.get(url)
    xRequestId = data.headers.get('X-Request-id')
    print(xRequestId)
