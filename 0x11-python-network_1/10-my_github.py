#!/usr/bin/python3

"""
a python script that takes github credentials as arguments and uses the github
api to display my id
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {password}"}

    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
