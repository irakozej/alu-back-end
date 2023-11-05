#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    # Fetch the user data
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch the tasks data
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Create a dictionary to store the tasks for each user
    user_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        user_tasks[user_id] = []
        for task in tasks:
            if task["userId"] == user_id:
                user_tasks[user_id].append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

    # Export the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)

    print("Data exported to todo_all_employees.json")

