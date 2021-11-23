"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask import Blueprint, jsonify, request, current_app
from .models import db, Card

api = Blueprint('api', __name__)

@api.route('/cards-info/', methods=['GET'])
def getCardsInfo():
    cards = Card.query.all()
    return jsonify({'cards': [r.to_dict() for r in cards]})
