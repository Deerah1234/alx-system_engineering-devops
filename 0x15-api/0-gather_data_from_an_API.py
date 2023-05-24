#!/usr/bin/python3

"""
    This module requests data from a RESTful API
    (https://jsonplaceholder.typicode.com/)
    and returns information about an employees tasks
"""

from requests import get
from sys import argv


def todo_progress():
    """ fetches the todo list progress for an employee """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
               .format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
               .format(argv[1])

    total_count = 0
    completed_count = 0
    completed_list = ''

    user_data = get(user_url).json()
    todo_data = get(todo_url).json()

    for task in todo_data:
        if task.get('completed') is True:
            completed_count += 1
            completed_list += "\t {}\n".format(task.get('title'))
        total_count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_data.get('name'), completed_count, total_count))
    print(completed_list, end="")


if __name__ == "__main__":
    todo_progress()
