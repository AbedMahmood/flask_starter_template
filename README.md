# Flask Starter Template
Barebone flask starter project with hybrid static/dynamic routing

### Virtual Environment (venv)
> Python -m venv venv

> source venv/bin/activate

> pip install -r requirements.txt

### Start Server
> flask run

### Stop Server
> ctrl + c

### Deactivate Venv
> deactivate

### Navbar
Found in templates/navbar.html

### Additional Pages
Adding pages to the project requires a few simple steps

1 - Make sure the page is added in the conig.py. This is to handle the dynamic part of the routing. If it isn't in config.py then routing will assume it is a dead link which routes to 404 page by default.

2 - Update the templates/navbar.html to include the link in the navigation menu options.

3 - create the html file within the templates/components/

Use templates/components/main.html as an example of how to correctly extend the base layout.

### KEYNOTE
In cofig.py components/main.html is referenced as 'home' so the word "Home" is displayed in the webpage instead of the word "Main".
