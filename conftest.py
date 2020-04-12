import pytest
import requests


@pytest.fixture()
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture()
def book_data():
    data = {"title": "111", "author": "0000"}
    return data


@pytest.fixture()
def init_book(base_url, book_data):
    r = requests.post(base_url+"books/", data=book_data)
    book = r.json()
    yield book
    requests.delete(base_url+f"books/{book['id']}")
