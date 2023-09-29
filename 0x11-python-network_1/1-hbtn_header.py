#!/usr/bin/python3
"""
a python script that takes in a URL and an email sends a request to the URL
"""

if __name__ == '__main__':
    """
    the script that sends request to the URL
    """
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-id'])
