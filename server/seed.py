
from .app import app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        
        r1 = Restaurant(name="Domino's Pizza", address="123 Main St")
        r2 = Restaurant(name="Pizza Palace", address="456 Junction Ave")
        
        
        p1 = Pizza(name="Hawaian", ingredients="Tomato, Mozzarella, Pineapple")
        p2 = Pizza(name="BBQ", ingredients="Tomato, Mozzarella, Steak")

        db.session.add_all([r1, r2, p1, p2])
        db.session.commit()

        
        db.session.add_all([
            RestaurantPizza(price=10, restaurant=r1, pizza=p1),
            RestaurantPizza(price=12, restaurant=r1, pizza=p2),
            RestaurantPizza(price=15, restaurant=r2, pizza=p1)
        ])
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()