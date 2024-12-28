# Flask Starter template for a static website
Flask starter template for hosting in pythonanywhere.com. This template is a basic starter template for building static websites (meaning just displaying pages and images and no complex routing required).

### Create virtual environment in local machine
> python -m venv venv

### Initiate venv in local machine
> venv source/bin/activate

### Create virtual environment in pythonanywhere
> mkvirtualenv venv --python=/usr/bin/python3.10

### VENV path in pythonanywhere
/home/username/.virtualenvs/venv

### Intiate venv in pythonanywhere
> workon venv

### Requirements
> pip install -r requirements.txt

### Deactivate VENV
> deactivate

### Navbar and page navigation
Navbar options for menu and overall site navigation pages which are allowed to navigate to are in my_config.py

### Additional pages for static website
1 - The pages which will be used for the site has to be registered in the allowed pages in my_config.py. This is to implement a basic control measure so not all pages are visible to everyone.

### Creating New Pages
1 - Create an HTML file within the `templates/pages/` directory.

2 - Use `templates/pages/main.html` as an example of how to correctly extend `layout.html`.
