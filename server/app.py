# Standard library imports
from flask import Flask, make_response, jsonify, request
# Remote library imports
from flask import request
from flask_restful import Resource
from datetime import datetime

# Local imports
from config import app, db
# Add your model imports
from models import db, Product, Price, CostOfInventory, Inventory, Customer, CustomerOrder, Sales

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)