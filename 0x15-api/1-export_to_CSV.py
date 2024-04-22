#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
and saves it to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, user_id)).json()
    username = user.get('username')
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

with open("{}.csv".format(user_id), "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow(
        [user_id, username, todo.get('completed'), todo.get('title')]
    )for todo in todos]
