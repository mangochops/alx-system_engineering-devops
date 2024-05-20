#!/usr/bin/python3
"""Exports data in JSON format for a given employee ID."""

import sys
import requests
import json

def get_employee_data(employee_id):
    """Fetches employee data from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
        return user_data, todos_data
    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
        sys.exit(1)

def export_to_json(user_data, todos_data):
    """Exports data to JSON format."""
    user_id = user_data.get('id')
    username = user_data.get('username')

    json_data = {str(user_id): []}
    for task in todos_data:
        json_data[str(user_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    json_file_name = f'{user_id}.json'
    with open(json_file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f'Data exported to {json_file_name}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_data, todos_data = get_employee_data(employee_id)
    export_to_json(user_data, todos_data)
