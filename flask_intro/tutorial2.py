# redirect and url_for are used for redirection to the desired page
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# functions are decorated with app.route
# render_template() is used for rendering template
@app.route("/")
def home():
    return render_template("index.html")

# How to pass arguemnt from tutorial2.py file to the frontend index.html
# <name> from the route is passed to the function, just make sure that while 
# writing render_template(...., some_variable = name) is passed. the name can be anything
@app.route("/<name>")
def print_name(name):
    return render_template("index.html", first_name = name)


#What if I want to pass a list to the backend
@app.route("/list")
def passing_list():
    return render_template("index.html", list_names = ["alisha", "sandro", "pascal", "nilu"])

# this is how we run our flask app
if __name__ == "__main__":
    app.run()