import pytest
import requests


data_list = [
    {"title": "112345    ", "author": "0235657"},
    {"title": "asdf sdfsd", "author": "hbjbsd sdfdsf"},
    {"title": "!@#$%^&*()", "author": "{}:\";'<?'}"},
    {"title": "ЯЧСМИваыва", "author": "ПМРМРМ ллрлрт"}
]


@pytest.mark.parametrize("data", data_list, ids=[str(item) for item in data_list])
def test_create_book(base_url, data):
    r = requests.post(base_url+"books/", data=data)
    assert r.status_code == 201
    r_body = r.json()
    data["id"] = r_body["id"]
    assert r_body == data


def test_update_book(base_url, init_book):
    data = {"title": "New Title", "author": "New Author"}
    r = requests.put(base_url+f"books/{init_book['id']}", data=data)
    assert r.status_code == 200
    r_body = r.json()
    data["id"] = r_body["id"]
    assert r_body == data
