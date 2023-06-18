#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        user = requests.get("{}/users/{}".format(BASE_URL, user_id)).json()
        tasks = requests.get("{}/todos?userId={}"
                             .format(BASE_URL, user_id)).json()
        completed_tasks = [task for task in tasks
                           if task.get("completed") is True]
        print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
              len(completed_tasks), len(tasks)))
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))
