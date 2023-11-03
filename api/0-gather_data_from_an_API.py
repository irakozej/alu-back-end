#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
    else:
        employee_id = argv[1]

        # Fetch user data
        user_response = requests.get(
               "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
           )
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch user's TODO list
        todo_response = requests.get(
          "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
                )
        todo_data = todo_response.json()

        # Calculate TODO progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task.get("completed"))

        # Print the progress
        print(
        "Employee {} is done with tasks({}/{}):".format
         (employee_name, completed_tasks, total_tasks))
        for task in todo_data:
            if task.get("completed"):
                print("\t {}".format(task.get("title")))

