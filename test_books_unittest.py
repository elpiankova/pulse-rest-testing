import requests
import unittest


class TestCreateBooks(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book_id = None

    def test_create_bok(self):
        book_data = {"title": "War and Peace", "author": "Lev Tolstoy"}
        r = requests.post(self.base_url+"books/", data=book_data)
        self.assertEqual(r.status_code, 201)
        r_body = r.json()
        self.assertIn("id", r_body.keys())
        ## Add "id" in book_data
        # book_data["id"] = r_body["id"]
        # self.assertEqual(book_data, r_body)
        ## Using for
        # for key in book_data:
        #     self.assertEqual(book_data[key], r_body[key])
        ## Deleting "id" from r_body
        self.book_id = r_body.pop("id")
        self.assertEqual(book_data, r_body)

    def tearDown(self):
        if self.book_id is not None:
            # TODO deleting
            print('\n', self.book_id)



