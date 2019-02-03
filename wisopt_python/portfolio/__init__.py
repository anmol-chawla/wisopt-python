from flask import Blueprint

# Create app and api objects for the Flask app
portfolio = Blueprint('portfolio', __name__)

from . import routes
