#!/usr/bin/python3
"""Sends a POST request with a letter and displays JSON response info"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
