#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
Example:
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        data = {}
        for employee in employees:
            employee_id = employee.get("id")
            todos = requests.get(
                url + "todos", params={"userId": employee_id}).json()
            username = employee.get("username", "")
            data["{employee_id}".format(employee_id=employee_id)] = [{
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed"),
            } for t in todos]
        json.dump(data, fp=jsonfile, sort_keys=False)
