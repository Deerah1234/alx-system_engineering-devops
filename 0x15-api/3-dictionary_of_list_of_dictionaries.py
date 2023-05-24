#!/usr/bin/python3

"""
    This module requests data from a RESTful API
    (https://jsonplaceholder.typicode.com/)
    and returns information about an all employees
    in JSON format
"""

from json import dump
from requests import get
from sys import argv


def todo_json_all():
    """ fetches the todo list progress for an employee """
    all_users_url = 'https://jsonplaceholder.typicode.com/users'

    total_count = 0
    completed_count = 0
    completed_list = ''

    user_data = get(all_users_url).json()

    full_list = {}
    i = 1
    for user in user_data:
        values = []
        todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
                   .format(i)
        todo_data = get(todo_url).json()
        for task in todo_data:
            current_task = {}
            current_task['task'] = task['title']
            current_task['completed'] = task['completed']
            current_task['username'] = user['username']
            values.append(current_task)
        full_list[user['id']] = values
        i += 1

    with open('todo_all_employees.json', 'w', encoding='utf-8') as tasksData:
        dump(full_list, tasksData)


if __name__ == "__main__":
    todo_json_all()
