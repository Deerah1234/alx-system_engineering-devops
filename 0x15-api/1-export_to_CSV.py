#!/usr/bin/python3

"""
    This module requests data from a RESTful API
    (https://jsonplaceholder.typicode.com/)
    and returns information about an employees tasks
    in a CSV format
"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


def todo_csv():
    """ fetches the todo list progress for an employee """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
               .format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
               .format(argv[1])

    user_data = get(user_url).json()
    todo_data = get(todo_url).json()

    with open('{}.csv'.format(user_data.get('id')), 'w',
              encoding='utf-8') as tasksData:
        taskWriter = writer(tasksData, quoting=QUOTE_ALL)
        for task in todo_data:
            taskWriter.writerow([user_data.get('id'),
                                 user_data.get('username'),
                                 task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    todo_csv()
