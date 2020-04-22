import pytest
import requests


@pytest.fixture()
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"


data_list = [
    {"title": "112345    ", "author": "0235657"},
    {"title": "asdf sdfsd", "author": "hbjbsd sdfdsf"},
    {"title": "!@#$%^&*()", "author": "{}:\";'<?'}"},
    {"title": "ЯЧСМИваыва", "author": "ПМРМРМ ллрлрт"}
]


@pytest.fixture(params=data_list, ids=[str(item) for item in data_list])
def book_data(request, base_url):
    data = request.param
    yield data
    if "id" in data:
        r = requests.delete(f"{base_url}books/{data['id']}")


@pytest.fixture()
def init_book(base_url, book_data):
    r = requests.post(base_url+"books/", data=book_data)
    book = r.json()
    yield book
    requests.delete(base_url+f"books/{book['id']}")
