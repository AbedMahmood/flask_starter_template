from flask import Flask, Blueprint, render_template, redirect, url_for
from config import Config

app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Define the blueprint
main_bp = Blueprint('main', __name__)

# Route for rendering the 404 page directly
@main_bp.route('/404')
def page_404():
    return render_page('components/404.html', 'Page Not Found')

# Helper function to render templates dynamically
def render_page(template_name, page_title, **context):
    return render_template(
        template_name,
        page_title=page_title,
        website_name=app.config['WEBSITE_NAME'],  # Access the website name from config
        year=app.config['YEAR'],  # Access the year from config
        **context  # This passes additional context variables to the template
    )

# Define the root route for the 'home' page
@main_bp.route('/')
@main_bp.route('/<page_name>')  # This will handle dynamic routes
def dynamic_page(page_name='home'):  # Default to 'home' if no page_name is provided
    # Get the template path from the config
    template = app.config['TEMPLATE_PATHS'].get(page_name)

    # If the template doesn't exist, redirect to the custom 404 page
    if not template:
        return redirect(url_for('main.page_404'))

    # Return the rendered template with a dynamic page title
    return render_page(template, page_name.capitalize())

# Register the blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
