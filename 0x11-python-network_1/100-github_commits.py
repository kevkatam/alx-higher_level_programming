#!/usr/bin/python3
"""
script that shows last ten commits of repo in github
"""
import sys
from requests import auth, get


if __name__ == '__main__':
    try:
        repo_name = sys.argv[1]
        owner = sys.argv[2]
        url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
        r = get(url)

        j = r.json()
        for commit in range(10):
            sha = j[commit].get('sha')
            author = j[commit].get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except Exception as e:
        pass
