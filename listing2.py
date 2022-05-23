import requests


class TodoException(Exception):
    pass


def find_todo(search: str, completed=True) -> list:
    validate(search)
    url = 'https://jsonplaceholder.typicode.com/todos'
    todos = get_resource(url)  # IO
    return filter_todos(search, completed, todos)


def filter_todos(search, completed, todos):
    return list(filter(lambda todo: search in todo['title'] and todo['completed'] is completed, todos))


def validate(search):
    if search == "":
        raise TodoException("search must not be empty")


def get_resource(url: str, getter=requests.get):
    try:
        response = getter(url)
    except Exception as e:
        raise TodoException("Error while getting resource", e)

    if response.status_code == 200:
        todos = response.json()
        return todos
    else:
        raise TodoException("GET error", response.status_code)
