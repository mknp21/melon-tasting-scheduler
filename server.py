"""Server for melon tasting scheduler app."""

from flask import (Flask, render_template, request, flash, json, session, redirect)
from model import connect_to_db

from jinja2 import StrictUndefined 
# from random import choice

import crud
# import requests
import json

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def show_home():
    """Show homepage."""

    return render_template("home.html")

@app.route("/", methods=["POST"])
def process_login():
    """Process user login info."""

    email = request.form.get("email")
    user = crud.get_user_by_email(email)

    if user == None:
        flash("No account found.")
        return redirect("/")
    else:
        session["current_user"] = user.user_id
        flash("Login successful!")
        return redirect("/browse-reservations")

@app.route("/browse-reservations")
def show_all_res():
    """Show available reservations."""

    return render_template("search.html")

@app.route("/reservations")
def show_user_res():
    """Show user's reservations."""

    user_id = session["current_user"]
    user = crud.get_user_by_id(user_id)

    return render_template("user_reservs.html", user=user)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)