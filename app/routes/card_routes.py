from flask import Blueprint, request, jsonify, make_response
from app.models.card import Card
from .routes_helper import make_class_safely, get_record_by_id
from app import db

bp = Blueprint("cards", __name__, url_prefix="/cards")

@bp.route("", methods=["GET"])
def get_all_cards():
    all_cards = Card.query.all()
    cards_as_dicts = [card.to_dict() for card in all_cards]

    return jsonify(cards_as_dicts)

@bp.route("/<card_id>", methods=["GET"])
def get_card_by_id(card_id):
    card = get_record_by_id(Card, card_id)
    return jsonify(card.to_dict())

@bp.route("/<card_id>/like", methods=["PATCH"])
def increase_card_like_count(card_id):
    card = get_record_by_id(Card, card_id)

    card.likes += 1
    db.session.commit()

    return jsonify(card.to_dict())