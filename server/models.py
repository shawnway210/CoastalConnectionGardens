# Models

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, func
from datetime import datetime, timedelta

from config import bcrypt,db

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String)

    price_id = db.Column(db.Integer, db.ForeignKey('prices.id', name='fk_product_prices'))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id', name='fk_product_prices'))

    serialize_rules = ('-price.product', '-inventory.product')

    price = db.relationship('Price', back_populates = 'product', uselist = False)
    inventory = db.relationship('Inventory', back_populates = 'product', uselist = False)

class Price(db.Model, SerializerMixin):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key = True)
    business_cost = db.Column(db.Float)
    customer_cost = db.Column(db.Float)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id', name='fk_price_product'))

    serialize_rules = ('-product.price', '-product.inventory')

    product = db.relationship('Product', back_populates = 'price', uselist =  False)
    cost_of_inventory = db.relationship('CostOfInventory', back_populates='price', uselist=False)

class CostOfInventory(db.Model, SerializerMixin):
    __tablename__ = 'costOfInventory'

    id = db.Column(db.Integer, primary_key = True)
    quantity_to_add = db.Column(db.Integer)
    cost = db.Column(db.Float)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id')) #many from class Product
    price_id = db.Column(db.Integer, db.ForeignKey('prices.id'))

    serialize_rules = ('-product.price', '-product.inventory', '-price.product')

    product = db.relationship('Product' , back_populates = 'cost_of_inventory', uselist=False)
    price = db.relationship('Price', back_populates='cost_of_inventory', uselist=False)

class Inventory(db.Model, SerializerMixin):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key = True)
    cost = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id', name='fk_price_product'))
    price_id = db.Column(db.Integer, db.ForeignKey('prices.id', name='fk_price_product'))
    cost_of_inventory_id = db.Column(db.Integer, db.ForeignKey('costOfInventory.id', name='fk_price_product'))

    serialize_rules = ('-product.price', '-product.inventory')

    product = db.relationship('Product', back_populates = 'inventory', uselist = False)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)

    customer_order_id = db.Column(db.Integer, db.ForeignKey('customerOrders.id'))

    serialize_rules = ('-customer_order.product', '-customer_order.customer')

    customer_order = db.relationship('CustomerOrder', back_populates = 'customer')

class CustomerOrder(db.Model, SerializerMixin):
    __tablename__ = 'customerOrders'

    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer)
    data_ordered = db.Column(db.Date)
    fullfilled = db.Column(db.Boolean)
    date_fullfulled = db.Column(db.Date)
    total_price = db.Column(db.Float)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    serialize_rules = ('-product.price', 'product.inventory', 'customer.customer_order')

    product = db.relationship('Product', back_populates = 'customer_order')
    customer = db.relationship('Customer', back_populates = 'customer_order')

class Sales(db.Model, SerializerMixin): 
    __tablename__  = 'sales'

    id = db.Column(db.Integer, primary_key = True)
    gross_sales = db.Column(db.Float)
    net_sales = db.Column(db.Float)

    customer_order_id = db.Column(db.Integer, db.ForeignKey('customerOrders.id'))
    innventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))

    serialize_rules = ('-customer_order.product', '-customer_order.customer', '-inventory.product')

    customer_order = db.relationship('CustomerOrder', back_populates='sales')
    inventory = db.relationship('Inventory', back_populates='sales')



