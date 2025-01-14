import os
from flask import Blueprint, render_template, current_app

bp = Blueprint('main', __name__)

@bp.route('/<page_name>')
@bp.route('/')
def main(page_name='home'):  # Default to 'home' if no page_name is provided
    templates_pages_dir = os.path.join(current_app.root_path, 'templates', 'pages')

    # Construct template path
    template_path = os.path.join(templates_pages_dir, f'{page_name}.html') if page_name != 'home' else os.path.join(templates_pages_dir, 'main.html')

    # Check if template exists
    if not os.path.exists(template_path):
        return render_template('pages/error.html', page_title="Error")

    # Compute relative path for Jinja2
    template_relative_path = os.path.relpath(template_path, os.path.join(current_app.root_path, 'templates'))
    return render_template(template_relative_path, page_title=page_name.capitalize())
