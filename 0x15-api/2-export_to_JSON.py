#!/usr/bin/python3
"""
Export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_Id = argv[1]

    link = "https://jsonplaceholder.typicode.com/users/{}".format(user_Id)
    response = requests.get(link)
    response_json = response.json()
    user_name = response_json.get('username')

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    response_json = response.json()

    todo_to_add = {"task": "TASK_TITLE", "completed": False,
                   "username": "USERNAME"}
    todos = []
    file_name = "{}.json".format(user_Id)

    with open(file_name, 'w') as f:
        for todo in response_json:
            if todo.get('userId') == int(user_Id):
                todo_to_add['task'] = todo.get('title')
                todo_to_add['completed'] = todo.get('completed')
                todo_to_add['username'] = user_name
                todos.append(todo_to_add.copy())
        result = {user_Id: todos}
        json.dump(result, f)
