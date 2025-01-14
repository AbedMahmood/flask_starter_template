import secrets
from flask import Flask
from app.router import bp

app = Flask(__name__, static_url_path='/static')

app.secret_key = secrets.token_hex(8)

# Register blueprints
app.register_blueprint(bp, url_prefix='/') 
