#!/usr/bin/python3
"""This Python script to export data in the JSON format."""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

    json_dict = {
        "{}".format(user_id): [
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username')
            } for todo in todos
        ]
    }
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(json_dict, jsonfile)
