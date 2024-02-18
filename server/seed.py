from app import app  # Assuming `app` is the Flask application instance
from models import db, Product, Price
# , CostOfInventory, Inventory, Customer, CustomerOrder, Sales



if __name__ == '__main__':
    with app.app_context():

        print('Starting Seed ...')

        db.session.query(Product).delete()
        db.session.query(Price).delete()
        # db.session.query(CostOfInventory).delete()
        # db.session.query(Inventory).delete()
        # db.session.query(Customer).delete()
        # db.session.query(CustomerOrder).delete()
        # db.session.query(Sales)

        product1 = Product(description='apple')

        product1price = Price(
            business_cost = 1.0,
            customer_cost = 2.0,
        )

        product1.price.append(product1price)
        
        db.session.add(product1)
        db.session.add(product1price)
        db.session.commit()

        print('Seed complete.')