from flask import Blueprint

# Create app and api objects for the Flask app
promotions = Blueprint('promotions', __name__)

from . import routes
