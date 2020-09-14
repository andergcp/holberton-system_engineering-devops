#!/usr/bin/python3
"""
Export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
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
    row = ['user_id', 'user_name', 'status', 'title']
    file_name = "{}.csv".format(user_Id)
    rows = []

    with open(file_name, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in response_json:
            if todo.get('userId') == int(user_Id):
                row[0] = user_Id
                row[1] = user_name
                row[2] = todo.get('completed')
                row[3] = todo.get('title')
                rows.append(row.copy())
        writer.writerows(rows)
