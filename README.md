# pizza-api-challenge

A simple REST API for managing pizza restaurants and their menus.

##   Start

1. Install dependencies:
```bash
pipenv install flask flask-sqlalchemy flask-migrate
pipenv shell
Set up database:

bash
export FLASK_APP=server/app.py
you can add a port => export FLASK_RUN_PORT=5000
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python -m server.seed

Run the server
bash
flask run

API will be available at http://localhost:5000

 API Endpoints
Restaurants
GET /restaurants - List all restaurants

GET /restaurants/<id> - Get restaurant details

DELETE /restaurants/<id> - Remove a restaurant

Pizzas
GET /pizzas - List all pizza types

Restaurant Pizzas
POST /restaurant_pizzas - Add pizza to a restaurant menu

 Examples
Get all restaurants:

bash
curl http://localhost:5000/restaurants
Add pizza to restaurant:

bash
curl -X POST http://localhost:5000/restaurant_pizzas \
-H "Content-Type: application/json" \
-d '{"price":10,"pizza_id":1,"restaurant_id":1}'
 
 RULES
1.Price must be between 1-30

2.All fields are required

3.Restaurant and pizza must exist

If you need to start fresh:

bash
rm -rf migrations
rm instance/pizza.db
flask db init
flask db migrate
flask db upgrade
python -m server.seed

  Testing with postman
Import the provided Postman collection

Set base URL to http://localhost:5000

Test endpoints in this order:

GET restaurants

GET pizzas

POST restaurant_pizzas

DELETE restaurant