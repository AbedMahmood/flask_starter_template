# Flask Starter template V1
Flask starter template for hosting in pythonanywhere.com. This template is a basic starter template for building a static website with multiple pages.

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

### Install flask
> pip install flask

### Starting Server
> flask run

### Deactivate VENV
> deactivate

### Creating New Pages
1 - Create an HTML file within the `templates/pages/` directory.

2 - Use `templates/pages/main.html` as an example of how to correctly extend `layout.html`.

### Router and Page Routing
In this version no need to worry about router. Just add html pages into the pages directory and router will automatically find the page and if the page isn't there router will default to the error.html. 

### Page Naming Convention
Have to use lower cases for example; main.html error.html test.html etc...