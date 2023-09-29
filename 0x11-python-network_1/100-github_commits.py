#!/usr/bin/python3

"""
a script that takes 2 arg in order to solve the problem that follows;
    first arg: repo name
    second arg: owner name

Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”

You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/

Print all commits by: `<sha>: <author name>` (one by line)
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    name = sys.argv[2]
    url = f"https://api.github.com/repos/{name}/{repo}/commits"

    content = requests.get(url)
    jsonData = content.json()

    for i in range(10):
        print(f"{jsonData[i]['sha']}: {jsonData[i]['commit']['author']['name']}") 
