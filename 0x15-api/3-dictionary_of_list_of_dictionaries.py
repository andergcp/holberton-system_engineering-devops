#!/usr/bin/python3
"""
Export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS},
 ... ],
"USER_ID": [ {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == '__main__':
    file_name = "todo_all_employees.json"

    link = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(link)
    users = response.json()

    link = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(link)
    todos_response = response.json()

    todo_to_add = {"task": "TASK_TITLE", "completed": False,
                   "username": "USERNAME"}
    todos = []
    users_todos = {}

    with open(file_name, 'w') as f:
        for user in users:
            for todo in todos_response:
                if todo.get('userId') == user.get('id'):
                    todo_to_add['task'] = todo.get('title')
                    todo_to_add['completed'] = todo.get('completed')
                    todo_to_add['username'] = user.get('username')
                    todos.append(todo_to_add.copy())
            users_todos.update({user.get('id'): todos.copy()})
            todos = []
        json.dump(users_todos, f)
