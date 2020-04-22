import requests

session = requests.Session()
session.auth = ("admin", "pass")

r_b = session.post("http://pulse-rest-testing.herokuapp.com/books2/", data={"title": "1", "author": "1"})
print(r_b.status_code)
r = session.post("http://pulse-rest-testing.herokuapp.com/roles2", data={
        "name": "Sergey Vdovichenko",
        "type": "Shcoder",
        "level": 80,
        "book": str(r_b.json()["id"])
    }
)
print(r.status_code)
print(r.json())
# r = session.get("http://pulse-rest-testing.herokuapp.com/roles2")
# print(r.json())
