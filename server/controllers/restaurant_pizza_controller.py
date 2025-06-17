from flask import request, jsonify
from server.models import db, Restaurant, Pizza, RestaurantPizza

def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    if not Restaurant.query.get(data['restaurant_id']):
        return jsonify({"error": "Restaurant not found"}), 404
    
    if not Pizza.query.get(data['pizza_id']):
        return jsonify({"error": "Pizza not found"}), 404
    
    rp = RestaurantPizza(
        price=price,
        restaurant_id=data['restaurant_id'],
        pizza_id=data['pizza_id']
    )
    db.session.add(rp)
    db.session.commit()
    return jsonify(rp.to_dict()), 201