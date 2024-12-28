from flask import Flask
from my_config import MyConfig

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'sdfwoif23fefd'  # Needed for flash messages
app.config.from_object(MyConfig)

# Add this line to make MyConfig methods accessible in templates
app.jinja_env.globals.update(config=MyConfig)

from app.routes import index

# Register blueprints
app.register_blueprint(index.bp)
