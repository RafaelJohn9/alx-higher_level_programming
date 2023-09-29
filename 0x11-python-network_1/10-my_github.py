#!/usr/bin/python3

"""
a python script that takes github credentials as arguments and uses the github
api to display my id
"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = {
            "Authorization": sys.argv[2]
            }

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, headers=password)

    content = response.json()
    print(content['id'])
