from app import app  # Assuming `app` is the Flask application instance
from models import db, Product, Price, CostOfInventory, Inventory, Customer, CustomerOrder, Sales



if __name__ == '__main__':
    with app.app_context():

        print('Starting Seed ...')

        db.session.query(Product).delete()
        db.session.query().delete()
        db.session.query().delete()
        db.session.query().delete()
        db.session.query().delete()
        db.session.query().delete()