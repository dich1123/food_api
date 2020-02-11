
Prerequisites
-
- Install everything from requirements.txt

Command: ~$ pip install -r requirements.txt

- API works with MySQL. You need create tables and set models.py

In models.py change line 9 for example: 'mysql://USER:PASSWORD@localhost/YOURDB'

Create tables: from python terminal

Command: ~$ from models import db
Command: ~$ db.create_all()

You can create random data. Run random_data_to_db.py
Command: ~$ python random_data_to_db.py



Installing
-
- Download all files to your computer
- Run builtin server
- Command: ~$ python api.py

Now you can do 4 operations:
- put. example: requests.put(URL+'order/orderid/foodid', json={'orderid': 'kek', 'address': 'Street 137',
 'customerid': '156', 'foodid': '2', 'quantity': '60'})

- get. example: requests.get(URL+'order/orderid/foodid')

- post. example: requests.post(URL+'order/orderid/foodid', json={'quantity': 17})

- delete. example: requests.delete(URL+'order/orderid/foodid') 

Where URL is your server. Example: 'http://127.0.0.1:5000/'

 Tests
 -
 
 Unittest tests main function for work with db.
 - Run command: ~$ python3 -m unittest discover
 
 Authors
 -
 -Cherenkov Dima(DiCh)