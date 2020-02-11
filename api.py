import models
from flask_restful import Api, Resource, reqparse
from flask import jsonify
import logging

""" Creating and setting logs variables"""
logger = logging.getLogger('api')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('logs/api.log')
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

handler2 = logging.StreamHandler()
handler2.setLevel(logging.INFO)
handler2.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(handler2)
logger.info('api works')

"""Creating Flask variables"""
db = models.db
app = models.app
api = Api(app)

parser = reqparse.RequestParser()


parser.add_argument('customerid')
parser.add_argument('address')
parser.add_argument('quantity')


class Order(Resource):
    """
    This class can do CRUD operations ONLY with orders (foodorder table)
    """

    def put(self, orderid, foodid):  # create new order element
        parsed = parser.parse_args()
        customerid = parsed['customerid']
        address = parsed['address']
        quantity = parsed['quantity']

        food = models.Food.query.get(int(foodid))
        if not food:
            logger.error(f"Order doesn't exists. ORDERID:{orderid}, FOODID:{foodid}")
            return '', 404

        quantity_left = int(food.quantity)
        price = int(food.price)
        total_price = price * int(quantity)

        order_in_table = models.Foodorder.query.filter_by(orderid=orderid, foodid=foodid).all()
        if order_in_table:
            logger.error(f'Order already exists. ORDERID:{orderid}, FOODID:{foodid}')
            return '', 500

        if int(quantity) > int(quantity_left):
            logger.error(f'Try of adding more food that we have. TRY:{quantity}, HAVE:{quantity_left}')
            return '', 500

        if (customerid is None) and (address is None):
            logger.error(f'Customerid or address required')
            return '', 500

        if address is None:
            customer = models.Customers.query.get(int(customerid))
            address = customer.address

        foodorder = models.Foodorder(orderid, foodid, customerid, address, quantity, total_price)
        try:
            db.session.add(foodorder)
            db.session.commit()
            logger.info('Order PUT: DONE')
            return '', 200

        except Exception:
            logger.error('Order PUT: FAILED')
            return '', 500

    def get(self, orderid, foodid):  # find all or one foodorder with orderid
        if str(foodid) == 'all':
            order = models.Foodorder.query.filter_by(orderid=orderid).all()
            try:
                full_order = {'orderid': orderid, 'customerid': order[0].customerid, 'address': order[0].address}
                orders = {}
                for i in range(len(order)):
                    orders[i] = {'foodid': order[i].foodid, 'quantity': order[i].quantity,
                                 'total_price': order[i].total_price}
                full_order['orders'] = orders
                logger.info('Order GET: DONE')
                return jsonify(full_order)
            except Exception:
                logger.error('Order GET: FAILED')
                return '', 500

        else:  # find one order
            order = models.Foodorder.query.filter_by(orderid=orderid, foodid=foodid).all()
            if not order:
                logger.error(f'Order GET: Order with ORDERID:{orderid}, FOODID{foodid} NOT FOUND')
                return '', 404

            try:
                full_order = {'orderid': str(orderid), 'customerid': str(order[0].customerid),
                              'address': str(order[0].address), 'foodid': str(order[0].foodid),
                              'quantity': str(order[0].quantity), 'total_price': str(order[0].total_price)}
                logger.info('Order GET: DONE')
                return jsonify(full_order)
            except Exception:
                logger.error('Order GET: FAILED')
                return '', 500

    def post(self, orderid, foodid):  # update existing order with orderid and foodid
        parsed = parser.parse_args()
        customerid = parsed['customerid']
        address = parsed['address']
        quantity = parsed['quantity']

        order = models.Foodorder.query.filter_by(orderid=orderid, foodid=foodid).all()
        if not order:
            logger.error(f'Order POST: Order with ORDERID:{orderid}, FOODID{foodid} NOT FOUND')
            return '', 404

        if customerid:
            order[0].customerid = customerid
        if address:
            order[0].address = address
        if quantity:
            order[0].quantity = quantity

        try:
            db.session.commit()
            logger.info('Order POST: DONE')
            return '', 201
        except:
            logger.error('Order POST: FAILED')
            return '', 500

    def delete(self, orderid, foodid):  # delete (all or one) existing orders. with orderid and foodid
        if str(foodid) == 'all':
            orders = models.Foodorder.query.filter_by(orderid=orderid).all()
        else:
            orders = models.Foodorder.query.filter_by(orderid=orderid, foodid=foodid).all()
        print(orders, '_______________')
        if not orders:
            logger.error(f'Order DELETE: Order with ORDERID:{orderid}, FOODID:{foodid} NOT FOUND')
            return '', 404

        try:
            for order in orders:
                db.session.delete(order)
                db.session.commit()
            logger.info('Order DELETE: DONE')
            return '', 204
        except Exception:
            logger.error('Order DELETE: FAILED')
            return '', 500


api.add_resource(Order, '/order/<orderid>/<foodid>')

if __name__ == '__main__':
    app.run(debug=True)
