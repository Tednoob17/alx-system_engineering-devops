#!/usr/bin/python3
"""
Save to JSON file
Dictionary of list of dictionaries
"""

import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    """Save to JSON file"""
    users = requests.get(BASE_URL + "/users").json()
    tasks = requests.get(BASE_URL + "/todos").json()
    user_dict = {}
    for user in users:
        user_dict[user.get("id")] = []
        for task in tasks:
            if task.get("userId") == user.get("id"):
                user_dict[user.get("id")].append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)
