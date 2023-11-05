#!/usr/bin/python3
"""
Gather data from an API and export to CSV
"""

import requests
import csv
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

        # Create a CSV file
        with open(f"{employee_id}.csv", mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            
            # Write header row
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write task data rows
            for task in todo_data:
                csv_writer.writerow([employee_id, employee_name, str(task.get("completed")), task.get("title")])
