#!/usr/bin/python3

"""
a python script that takes in a URL and an email,
sends a POST  request to the passed URL
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
