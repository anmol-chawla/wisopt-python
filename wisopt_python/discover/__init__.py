from flask import Blueprint

# Create app and api objects for the Flask app
portfolio = Blueprint('discover', __name__)

from . import routes
