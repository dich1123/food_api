import random
import models

food1 = ['L', ['juice', 'milk', 'water', 'whiskey', 'cola']]  # queen of dance floor
food2 = ['KG', ['potato', 'onion', 'meat', 'cheese']]
food3 = ['PC', ['snickers', 'milkslice', 'mars', 'bounty']]

names = ['Dima', 'Kate', 'Nick', 'Flash', 'Hulk', 'Meatboy']
addresses = ['Street 5', 'Street 51', 'Street 178', 'Street 125', 'Street 545', 'Street 23']
phone_codes = ['+38095', '+38099', '+38073']

for i in range(500):  # put customers into db
    phone = random.choice(phone_codes) + str(random.randint(1000000, 9999999))
    name = random.choice(names)
    address = random.choice(addresses)
    customer = models.Customers(name, phone, address)
    models.db.session.add(customer)
    models.db.session.commit()

for i in range(731):
    food_l = random.choice([food1, food2, food3])
    measurement = food_l[0]
    name = random.choice(food_l[1])
    quantity = random.randint(0, 1000)
    price = random.randint(10, 100)
    food = models.Food(name, quantity, measurement, price)
    models.db.session.add(food)
    models.db.session.commit()
