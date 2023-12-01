#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == '__main__':
    data = {'q': ""}
    try:
        data['q'] = sys.argv[1]
    except Exception as e:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        j = r.json()
        if not j:
            print("No result")
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except Exception as e:
        print("Not a valid JSON")
