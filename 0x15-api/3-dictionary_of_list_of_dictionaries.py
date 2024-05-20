#!/usr/bin/python3
"""
Export data in JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users_response = requests.get(users_url)
    todos = response.json()
    users = users_response.json()

    all_tasks = {}
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [{'username': username,
                       'task': task['title'],
                       'completed': task['completed']}
                      for task in todos if task['userId'] == user['id']]
        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)
