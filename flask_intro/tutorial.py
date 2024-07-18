# redirect and url_for are used for redirection to the desired page
from flask import Flask, redirect, url_for


app = Flask(__name__)

# functions are decorated with app.route
@app.route("/")
def home():
    return "Hello this is the main page <H1> HELLO </h1>"

# When we put something in <> it can grab values and pass that in the function
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


# When defining redirect function we have to define the name of the function as argument
@app.route("/admin")
def admin():
    # why did we add 'name' argument below? because we want to pass a value for our user function defined above
    return redirect(url_for("user", name = "some argument here"))

# this is how we run our flask app
if __name__ == "__main__":
    app.run()