import pytest
from requests import Response, TooManyRedirects
from listing2 import TodoException, filter_todos, find_todo, get_resource, validate


def test_find_todo_valid_search():
    todos = find_todo("autem")
    assert len(todos) > 0
    assert all(["autem" in todo['title'] for todo in todos])
    assert all([todo['completed'] is True for todo in todos])


def test_validate():
    with pytest.raises(TodoException):
        validate("")


def test_filter_todos():
    todos = [
        {
            "userId": 1,
            "id": 20,
            "title": "ullam nobis libero sapiente ad optio sint",
            "completed": True
        },
        {
            "userId": 2,
            "id": 21,
            "title": "suscipit repellat esse quibusdam voluptatem incidunt",
            "completed": False
        },
    ]

    assert filter_todos("other word", True, todos) == []
    assert filter_todos("", True, todos)[0] == todos[0]
    assert filter_todos("", False, todos)[0] == todos[1]


def test_get_resource():
    def get_500(*args, **kwargs):
        response = Response()
        response.status_code = 500
        return response

    def get_error(*args, **kwargs):
        raise TooManyRedirects()

    with pytest.raises(TodoException):
        get_resource("url", getter=get_500)
        get_resource("url", getter=get_error)
