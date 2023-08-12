import unittest
from task2 import MoviesDatabase

class TestAPI(unittest.TestCase):

    def mod(self):
        dec = MoviesDatabase('https://moviesdatabase.p.rapidapi.com/actors/random',
                             '1b14d6fd0cmshf21c659eee42808p1c174ajsn8c234f908767',
                             'moviesdatabase.p.rapidapi.com')
        return dec

    def test_status(self, num_querys=2):
        self.assertEqual(self.mod().respon(num_querys).status_code, 200, 'is wrong')

    def test_entries(self):
        self.assertEqual(self.mod().get_res_json(2)['entries'], 2, 'is wrong')

    def test_result(self):
        self.assertEqual(type(self.mod().get_res_json(2)), dict, 'is wrong')

    def test_content_type(self):
        self.assertEqual(self.mod().respon(2).headers['Content-Type'],
                         'application/json; charset=utf-8', 'is wrong')

    def test_querystring(self):
        self.assertEqual(self.mod().querystring(2), {'limit': {2}}, 'is wrong')
