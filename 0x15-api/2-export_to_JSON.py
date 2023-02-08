#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID":
[{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    username = employee.get("username", "")

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({"{employee_id}".format(employee_id=employee_id): [{
            "task": t.get("title"), "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
