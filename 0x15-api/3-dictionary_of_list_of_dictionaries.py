#!/usr/bin/python3
"""
    a Python script for a given employee ID, returns information
    about his/her TODO list progress. then will
    export data in the json format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    """
    a Python script for a given employee ID, returns information
    about his/her TODO list progress. using json format.
    """
    strcont = len(sys.argv) - 1
    if strcont > 1:
        print("please only employeid")
        sys.exit(1)
    elif strcont <= 0:
        empcode = ""
    else:
        if sys.argv[1]:
            empcode = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    headers = {
        "Content-Type": "application/json",
        }
    user = requests.get(url + "users/{}".format(empcode))
    todos = requests.get(url + "todos", params={"userId": empcode})
    user = user.json()
    todos = todos.json()

    with open("todo_all_employees.json", "w", newline="") as jfile:
        json.dump({
            data.get("id"): [{
                "username": datad.get("username"),
                "task": datad.get("title"),
                "completed": datad.get("completed")
            }
                for datad in requests.get(url + "todos",
                                          params={"userId":
                                                  data.get("id")}).json()]
            for data in user}, jfile)
