#!/usr/bin/python3
"""Gathers data from a given REST API endpoint."""

import sys
import requests

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

def format_output(user_data, todos_data):
    """Formats and prints the output."""
    completed_tasks = [task['title'] for task in todos_data if task['completed']]
    total_tasks = len(todos_data)
    employee_name = user_data.get('name', 'Unknown')

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_data, todos_data = get_employee_data(employee_id)
    format_output(user_data, todos_data)
