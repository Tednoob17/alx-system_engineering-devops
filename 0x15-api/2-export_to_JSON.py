#!/usr/bin/python3
"""Export to JSON file"""

import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        user = requests.get("{}/users/{}".format(BASE_URL, user_id)).json()
        tasks = requests.get("{}/todos?userId={}"
                             .format(BASE_URL, user_id)).json()
        user_dict = {user_id: [{"task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": user.get("username")}
                               for task in tasks]}
        with open('{}.json'.format(user_id), 'w') as f:
            json.dump(user_dict, f)
