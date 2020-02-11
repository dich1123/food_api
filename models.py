from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:Hardpas!1123@localhost/fooddb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asdgcvbk;SLDCN;'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Customers(db.Model):
    """
    Creating and exploring customer table
    """
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    phone = db.Column('phone', db.String(100), nullable=False)
    address = db.Column('address', db.String(100), nullable=False)

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f'Customers name:{self.name}, phone:{self.phone}, address:{self.address}'


class Food(db.Model):
    """
    Creating and exploring food table
    """
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    measurement = db.Column('measurement', db.String(10), nullable=False)
    price = db.Column('price', db.Integer, nullable=False)

    def __init__(self, name, quantity, measurement, price):
        self.name = name
        self.quantity = quantity
        self.measurement = measurement
        self.price = price

    def __repr__(self):
        return f'Food name:{self.name},quantity:{self.quantity},measurement{self.measurement},' \
               f'price:{self.price}'


class Foodorder(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    orderid = db.Column('orderid', db.String(100), nullable=False)  # unique key for each order.saves in cookies
    foodid = db.Column('foodid', db.Integer, db.ForeignKey('food.id'))
    customerid = db.Column('customerid', db.Integer, db.ForeignKey('customers.id'), nullable=True)
    address = db.Column('address', db.String(150), nullable=False)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    total_price = db.Column('total_price', db.Integer, nullable=False)
    time = db.Column('time', db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, orderid, foodid, customerid, address, quantity, total_price):
        self.orderid = orderid
        self.foodid = foodid
        self.customerid = customerid
        self.address = address
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self):
        return f'Foodorder orderid:{self.orderid}, foodid:{self.foodid}, customerid:{self.customerid}, ' \
               f'address:{self.address}, quantity:{self.quantity}, total_price:{self.total_price}'


if __name__ == '__main__':
    manager.run()
