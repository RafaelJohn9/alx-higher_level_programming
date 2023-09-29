#!/usr/bin/python3

"""
a python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
