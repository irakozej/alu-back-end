#!/usr/bin/python3
"""
Gather data from an API and export to JSON
"""

import requests
import json
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
        employee_name = user_data.get("username")

        # Fetch user's TODO list
        todo_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        )
        todo_data = todo_response.json()

        # Create a dictionary to store tasks data
        tasks_data = {employee_id: []}

        # Populate tasks_data with task information
        for task in todo_data:
            tasks_data[employee_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            })

        # Save data to a JSON file
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(tasks_data, json_file)
