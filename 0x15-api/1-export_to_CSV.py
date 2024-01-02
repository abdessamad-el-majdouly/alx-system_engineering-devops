#!/usr/bin/python3
"""
    a Python script for a given employee ID, returns information
    about his/her TODO list progress. then will
    export data in the CSV format.
"""
import csv
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

    with open("{}.csv".format(empcode), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [empcode, user.get("username"), data.get("completed"),
             data.get("title")]
         ) for data in todos]
