#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    username = employee.get("username", "")

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [employee_id, username, t.get("completed"), t.get("title")])
