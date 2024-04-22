#!/usr/bin/python3
"""
Module to interact with a REST API and manipulate data

"""


import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

with open("{}.csv".format(user_id), "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow([user_id, user.get('username'),
                      todo.get('completed'), todo.get('title')])
     for todo in todos]
