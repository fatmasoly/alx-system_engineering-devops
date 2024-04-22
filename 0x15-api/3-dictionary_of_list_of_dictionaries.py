#!/usr/bin/python3
"""This Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}users".format(url)).json()
    todos = requests.get("{}todos".format(url)).json()

    json_dict = {
        "{}".format(user.get("id")): [
            {
                "username": user.get('username'),
                "task": todo.get('title'),
                "completed": todo.get('completed'),
            } for todo in todos if user.get('id') == todo.get('userId')
        ]for user in users
    }
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
