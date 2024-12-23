# app/__init__.py
from flask import Flask
from .routes import main_bp  # Import from app/routes/__init__.py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
