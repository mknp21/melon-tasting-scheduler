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


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)