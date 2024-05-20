#!/usr/bin/python3
"""Exports data in CSV format for a given employee ID."""

import sys
import requests
import csv

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

def export_to_csv(user_data, todos_data):
    """Exports data to CSV format."""
    user_id = user_data.get('id')
    username = user_data.get('username')

    csv_file_name = f'{user_id}.csv'
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed_status = task['completed']
            task_title = task['title']
            csv_writer.writerow([user_id, username, str(task_completed_status), task_title])

    print(f'Data exported to {csv_file_name}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_data, todos_data = get_employee_data(employee_id)
    export_to_csv(user_data, todos_data)
