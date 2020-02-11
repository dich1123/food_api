import requests

URL = 'http://127.0.0.1:5000/'

r = requests.put(URL+'order/fun/128', json={'orderid': 'kek', 'address': 'Street 137', 'customerid': '156', 'foodid': '2', 'quantity': '60'})
print(r, '\n')

r = requests.get(URL+'order/fun/128')
print(r, '\n', r.content, '\n')

r = requests.post(URL+'order/fun/128', json={'quantity': 17})
print(r, '\n')

r = requests.delete(URL+'order/fun/128')
print(r, '\n')
