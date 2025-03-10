import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.card import Card
    from app.models.board import Board

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import board_routes, card_routes

    app.register_blueprint(board_routes.bp)
    app.register_blueprint(card_routes.bp)

    CORS(app)
    return app
