#!/usr/bin/python3
"""Returns information about user TODO list progress."""
import requests
from sys import argv

if __name__ == '__main__':
    user_Id = argv[1]
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    response_json = response.json()

    total_todos = 0
    completed_todos = 0
    completed_todos_list = []

    for todo in response_json:
        if todo.get('userId') == int(user_Id):
            if todo.get('completed') is True:
                completed_todos += 1
                completed_todos_list.append(todo.get('title'))
            total_todos += 1

    link = "https://jsonplaceholder.typicode.com/users/{}".format(user_Id)
    response = requests.get(link)
    response_json = response.json()
    user_name = response_json.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_todos, total_todos))
    for todo in completed_todos_list:
        print("\t {}".format(todo))
