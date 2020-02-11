import unittest
import requests

URL = 'http://127.0.0.1:5000/'


class TestRest(unittest.TestCase):

    def test_put(self):
        r = requests.put(URL+'order/kek/129', json={'orderid': 'kek', 'address': 'Street 137',
                                                    'customerid': '156', 'foodid': '2', 'quantity': '60'})
        print(r.status_code)
        self.assertEqual(r.status_code, 200)

    def test_get_one(self):
        r = requests.put(URL + 'order/kek/127', json={'orderid': 'kek', 'address': 'Street 137',
                                                      'customerid': '156', 'foodid': '2', 'quantity': '60'})
        r = requests.get(URL + 'order/kek/127')
        self.assertEqual(r.status_code, 200)

    def test_get_all(self):
        r = requests.put(URL + 'order/kek/127', json={'orderid': 'kek', 'address': 'Street 137',
                                                      'customerid': '156', 'foodid': '2', 'quantity': '60'})
        r = requests.get(URL + 'order/kek/all')
        self.assertEqual(r.status_code, 200)

    def test_post(self):
        r = requests.put(URL + 'order/kek/127', json={'orderid': 'kek', 'address': 'Street 137',
                                                      'customerid': '156', 'foodid': '2', 'quantity': '60'})
        r = requests.post(URL + 'order/kek/127', json={'quantity': 17})
        self.assertEqual(r.status_code, 201)

    def test_delete_one(self):
        r = requests.put(URL + 'order/kek/127', json={'orderid': 'kek', 'address': 'Street 137',
                                                      'customerid': '156', 'foodid': '2', 'quantity': '60'})
        r = requests.delete(URL + 'order/kek/127')
        self.assertEqual(r.status_code, 204)

    def test_delete_all(self):
        r = requests.put(URL + 'order/kek/127', json={'orderid': 'kek', 'address': 'Street 137',
                                                      'customerid': '156', 'foodid': '2', 'quantity': '60'})
        r = requests.delete(URL + 'order/kek/all')
        self.assertEqual(r.status_code, 204)
