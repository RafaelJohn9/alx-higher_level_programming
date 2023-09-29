#!/usr/bin/python3

"""
a python script that takes in a url
and an email address sends a POST requst to the passed
URL with the email as a parameter,
and finally displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {
            "email": email
            }
    content = requests.post(url, data=data)
    print(content)
