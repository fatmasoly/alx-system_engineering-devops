#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

    filter_todo = [todo for todo in todos if todo.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'),
                  len(filter_todo),
                  len(todos)))

    [print("\t {}".format(todo.get('title'))) for todo in filter_todo]
