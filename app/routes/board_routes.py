from flask import Blueprint, request, jsonify, make_response
from app.models.board import Board
from app.models.card import Card
from .routes_helper import make_class_safely, get_record_by_id
from app import db

bp = Blueprint("boards", __name__, url_prefix="/boards")

@bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = make_class_safely(Board, request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify(new_board.to_dict()), 201

@bp.route("", methods=["GET"])
def get_all_boards():
    all_boards = Board.query.all()
    boards_as_dicts = [board.to_dict() for board in all_boards]

    return jsonify(boards_as_dicts)

@bp.route("/<board_id>", methods=["GET"])
def get_board_by_id(board_id):
    board = get_record_by_id(Board, board_id)
    return jsonify(board.to_dict())

@bp.route("/<board_id>/cards", methods=["POST"])
def add_card_to_board(board_id):
    board = get_record_by_id(Board, board_id)

    request_body = request.get_json()
    request_body["board"] = board
    new_card = make_class_safely(Card, request_body)

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201

@bp.route("/<board_id>", methods=["DELETE"])
def delete_card_by_id(board_id):
    board = get_record_by_id(board_id)
    
    db.session.delete(board)
    db.session.commit()

    msg = f"Board with id {board_id} successfully deleted!"
    return make_response(msg)