from flask import request, jsonify
from server.models import db, Restaurant

def get_all():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200


def get(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict(with_pizzas=True))


def delete(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
