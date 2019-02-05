from flask import Flask, Blueprint
from flask_restplus import Api
api_bp = Blueprint('api', __name__)
api = Api(api_bp, version='1.0', title='Wisopt_Python', description='All the python APIs under one roof', doc='/info/')
app = Flask(__name__, instance_relative_config=True)
portfolio_apis = api.namespace('portfolio', description='APIs dealing with the portfolio of a user')


def create_app():
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    from .portfolio import portfolio as portfolio_blueprint
    app.register_blueprint(portfolio_blueprint)
    app.register_blueprint(api_bp)
    return app
