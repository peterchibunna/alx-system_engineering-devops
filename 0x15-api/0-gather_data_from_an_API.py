#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    output = "Employee {EMPLOYEE_NAME} is done " \
             "with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    done_tasks = [t.get("title") for t in todos if t.get("completed", False)]
    print(output.format(
        EMPLOYEE_NAME=employee.get("name"),
        NUMBER_OF_DONE_TASKS=len(done_tasks),
        TOTAL_NUMBER_OF_TASKS=len(todos)))
    for c in done_tasks:
        print("\t {}".format(c))
