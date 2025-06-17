from flask import jsonify
from server.models import Pizza

def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])