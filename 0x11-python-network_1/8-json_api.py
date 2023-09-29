#!/usr/bin/python3

"""
a python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    content = requests.post(url, data=data)

    try:
        jsonData = content.json()

        if jsonData:
            print(f"[{jsonData.get('id')}] {jsonData.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
