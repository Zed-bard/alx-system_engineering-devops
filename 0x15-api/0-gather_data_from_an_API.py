#!/usr/bin/python3
""" Script to get TODO list progress
    by employee ID
"""
from requests import get
from sys import argv


def todo(emp_id):
    """ Send request for employee's
        to do list to API
    """
    total = 0
    completed = 0
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'

    # Check if user exists
    user_response = get(url_user + emp_id)
    if user_response.status_code != 200:
        print("Error: Employee ID not found or API request failed")
        return
    user = user_response.json().get('name')

    if user:
        params = {'userId': emp_id}
        #  get all tasks
        tasks_response = get(url_todo, params=params)
        if tasks_response.status_code != 200:
            print("Error: Failed to fetch TODO list")
            return
        tasks = tasks_response.json()
        if tasks:
            total = len(tasks)
            #  get number of completed tasks
            params.update({'completed': 'true'})
            completed = len(get(url_todo, params=params).json())

        # Adjust employee name if it's too long
        if len(user) > 18:
            user = user[:15] + "..."
        print("Employee Name: {} is done with tasks({}/{}):".format(
            user, completed, total))
        for task in tasks:
            if task.get('completed') is True:
                print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    if len(argv) > 1:
        todo(argv[1])

