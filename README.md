# Overview

Flask Intro Todo app (Basic CRUD app)

ToDo application which allows to add a task in the table and once the task is done, there's an option to delete the task from the list.

An update feature should allow an existing todo to update.


## Requirements

Python

Pip

Virtual env


Create a virtual python virtual env: python3 -m venv env

Activate this python env: source env/bin/activate

Install flask and related libraries: pip3 install flask flask-sqlalchemy

Create an app.py file for flask application

Template inheritance

- Create one master html file which is a skeleton file which is inherited by other pages.
- So we don't have to write the boiler plate again and again

Flask requires an application context to access certain functionalities, including database operations.

https://flask.palletsprojects.com/en/2.3.x/appcontext/


Initializing the DB

Instead of Running the db.create_all() command in the terminal Initialize the Database in your code after your Database Models classes have been setup:
with app.app_context():
        db.create_all()

Basically, put this in your Flask app under the Db.Model classes. Make sure to indent properly and run your flask app one time. It should create the database (also check your instance folder for the db file). Then comment it out. You can run other SQL commands under the with statement if you need info on what's in your database file.
