from flask import Flask
from flask_migrate import Migrate
from server import db
from server.controllers import (
    restaurant_controller,
    pizza_controller,
    restaurant_pizza_controller
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return restaurant_controller.get_all_restaurants()

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant(id):
    return restaurant_controller.handle_restaurant(id, request.method)

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    return pizza_controller.get_all_pizzas()

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    return restaurant_pizza_controller.create_restaurant_pizza()