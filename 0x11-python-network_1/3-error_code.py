#!/usr/bin/python3

"""
a python script tthat takes in a URL sends a request to the URL and displays
the body of the response(decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
