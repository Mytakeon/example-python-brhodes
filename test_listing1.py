from unittest import mock
import pytest
from listing1 import TodoException, find_todo


def test_find_todo_valid_search():
    todos = find_todo("autem", True)
    assert len(todos) > 0
    assert all(["autem" in todo['title'] for todo in todos])
    assert all([todo['completed'] is True for todo in todos])


def test_find_todo_no_results():
    todos = find_todo("something something", True)
    assert len(todos) == 0


def test_find_todo_empty_query():
    with pytest.raises(TodoException):
        find_todo("")


def test_find_server_error():
    # mock the requests.get() method to return a 500 error
    with mock.patch('listing1.requests.get', side_effect=Exception("Server error")):
        with pytest.raises(TodoException):
            find_todo("autem")
