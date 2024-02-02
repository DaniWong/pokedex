# Pokedex Back End

This is a back end component for the Pokedex project.
Stack: Python, Django, sqlite

## How to run the application?

In the project directory, you can run:

### `pip install -r requirements.txt`

Installs all requirements for the app.

### `python manage.py migrate`

Applies all migrations needed in the database.

### `python manage.py runserver`

Runs the app in the debug mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

Note: You can access to django admin just open [http://localhost:8000/admin](http://localhost:8000/admin) to view it.
For to be able to access you need to create a super user with python manage.py createsuperuser.

## Additional scripts

### `python manage.py test`

Launches all avilable tests.
Test are available: For check api rest and api pokemon. 
