#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import requests
import sys


url = "https://jsonplaceholder.typicode.com/users"
user_id = int(sys.argv[1])
user = requests.get("{}users/{}".format(url, user_id)).json()
todos = requests.get("{}todos?userId={}".format(url, user_id)).json()

filter_todo = list(filter(lambda x: x.get('completed') is True, todos)).json()

print("Employee {} is done with tasks({}/{}):"
      .format(user.get('name'),
              len(filter_todo),
              len(todos)))

[print("\n".join("\t {}".format(todo.get('title')) for todo in filter_todo))]


if __name__ == "__main__":
