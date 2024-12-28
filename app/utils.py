from flask import render_template
from app import app
import os

def get_css_file(template_name):
    """Return the corresponding CSS file name based on the template name."""
    base_name = os.path.splitext(template_name)[0]  # Get the base name without extension
    return f"{base_name}.css"  # Return corresponding CSS file name

def render_page(template_name, page_title, **context):
    css_file = get_css_file(template_name)  # Get the corresponding CSS file
    return render_template(
        template_name,
        page_title=page_title,
        website_name=app.config['WEBSITE_NAME'],
        year=app.config['YEAR'],
        css_file=css_file,  # Pass the CSS file to the template
        **context
    )
