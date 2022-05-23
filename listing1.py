import requests


class TodoException(Exception):
    pass


def find_todo(search: str, completed=True) -> list:
    if search == "":
        raise TodoException("search must not be empty")

    try:
        url = 'https://jsonplaceholder.typicode.com/todos'
        response = requests.get(url)
    except Exception as e:
        raise TodoException("Error while getting resource", e)

    if response.status_code == 200:
        todos = response.json()
        return list(filter(lambda todo: search in todo['title'] and todo['completed'] is completed, todos))
    else:
        raise TodoException("Error while getting todos", response.status_code)
