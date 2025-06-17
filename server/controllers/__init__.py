from flask import jsonify
from server.models import db, Restaurant

def get_all_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

def handle_restaurant(id, method):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    if method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    
    return jsonify(restaurant.to_dict(with_pizzas=True))