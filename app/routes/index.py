import os
from flask import Blueprint, redirect, url_for, current_app
from app.utils import render_page
from my_config import MyConfig

bp = Blueprint('main', __name__)

@bp.route('/error')
def error():
    return render_page('pages/error.html', "Error")

@bp.route('/')
@bp.route('/<page_name>')
def main(page_name='home'):
    # Check if the requested page is in the allowed pages
    if page_name not in MyConfig.ALLOWED_PAGES:
        return redirect(url_for('main.error'))

    if page_name == 'home':
        template_path = 'pages/main.html'
    else:
        template_path = f'pages/{page_name}.html'
    
    template_full_path = os.path.join(current_app.root_path, 'templates', template_path)
    
    if os.path.exists(template_full_path):
        return render_page(template_path, page_name.capitalize())
    else:
        return redirect(url_for('main.error_page'))

