#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        csv_content = []
        user_id = sys.argv[1]
        user = requests.get("{}/users/{}".format(BASE_URL, user_id)).json()
        tasks = requests.get("{}/todos?userId={}"
                             .format(BASE_URL, user_id)).json()
        for task in tasks:
            csv_content.append([user_id, user.get("username"),
                                task.get("completed"), task.get("title")])
        with open('{}.csv'.format(user_id), 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(csv_content)
