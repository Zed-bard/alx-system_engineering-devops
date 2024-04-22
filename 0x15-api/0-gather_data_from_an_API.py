#!/usr/bin/python3
import requests
import sys

def get_employee_progress(employee_id):
    # Base URL for the API
    api_url = "https://jsonplaceholder.typicode.com"

    # Get the user data
    user_url = f"{api_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get the TODO list for the user
    todos_url = f"{api_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Print out the employee progress
    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")

    # Print out the titles of completed tasks
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_employee_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: python3 script.py <employee_id>")
