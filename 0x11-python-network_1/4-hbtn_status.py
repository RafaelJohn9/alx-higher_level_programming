#!/usr/bin/python3

"""
a python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
