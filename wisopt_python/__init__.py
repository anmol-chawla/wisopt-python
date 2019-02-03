from flask import Flask, Blueprint
from flask_restful import Api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app = Flask(__name__, instance_relative_config=True)


def create_app():
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    from .portfolio import portfolio as portfolio_blueprint
    app.register_blueprint(portfolio_blueprint)
    app.register_blueprint(api_bp)
    return app
