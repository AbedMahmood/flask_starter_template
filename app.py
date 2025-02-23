import secrets
import os
from flask import Flask, render_template, send_from_directory, url_for, abort

app = Flask(__name__, template_folder='pages')
app.secret_key = secrets.token_hex(8)

@app.route('/<page_name>')
@app.route('/')
def main(page_name='home'):
    html_file = f'{page_name}/{page_name}.html'
    css_file = f'{page_name}.css'
    js_file = f'{page_name}.js'

    css_url = url_for('serve_css', filename=f'{page_name}/{css_file}')
    js_url = url_for('serve_js', filename=f'{page_name}/{js_file}')

    print(f"CSS URL: {css_url}")
    print(f"JS URL: {js_url}")

    try:
        return render_template(
            html_file,
            page_title=page_name.capitalize(),
            css_file=css_url,
            js_file=js_url
        )
    except Exception as e:
        abort(404)

@app.route('/css/<path:filename>')
def serve_css(filename):
    try:
        return send_from_directory(os.path.join(app.root_path, 'pages'), filename)
    except FileNotFoundError:
        abort(404)

@app.route('/js/<path:filename>')
def serve_js(filename):
    try:
        return send_from_directory(os.path.join(app.root_path, 'pages'), filename)
    except FileNotFoundError:
        abort(404)

@app.route('/pages/layout.css')
def serve_layout_css():
    try:
        return send_from_directory(os.path.join(app.root_path, 'pages'), 'layout.css')
    except FileNotFoundError:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '/error/error.html',
        page_title="Error",
        error_message="Page not found",
        css_file=url_for('serve_css', filename='error/error.css'),
        js_file=url_for('serve_js', filename='error/error.js')
    ), 404

if __name__ == '__main__':
    app.run(debug=True)
