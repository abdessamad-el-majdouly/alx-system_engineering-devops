#!/usr/bin/python3
"""
    a Python script for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    """
    a Python script for a given employee ID, returns information
    about his/her TODO list progress.
    """
    strcont = len(sys.argv) - 1
    if strcont > 1 or strcont <= 0:
        print("please only employeid")
        sys.exit(1)
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

    done = [data.get("title") for data in todos
            if data.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    [print("\t {}".format(c)) for c in done]
