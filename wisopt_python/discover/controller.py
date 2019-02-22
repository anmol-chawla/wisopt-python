from flask import request, abort, jsonify
from flask_restplus import Resource

from ..common.authenticate import verify_token
from .models.fetch import return_articles
from .models.insertions import insert_articles
from .. import discover_apis as api


# Declaring a base parser object with the arguments required for each route
base_parser = api.parser()
base_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')
base_parser.add_argument(
    'user_id', type=int, location='args', required=True, help='User ID')

# Declaring a parser object for inserting data with the necessary arguments
fetchArticle_parser = base_parser.copy()
fetchArticle_parser.add_argument(
    'search_term', type=str, location='args', required=True, help='The term for which articles need to be fetched')


class Articles(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=fetchArticle_parser)
    @api.response(201, 'JSON response')
    @api.response(401, 'Unauthorized access')
    def get(self):
        '''
            Get the articles for a particular term
        '''
        try:
            search_term = request.args.get('search_term')
            data = return_articles(search_term)
            return jsonify(data)
        except Exception as e:
            abort(400, str(e))

    def post(self):
        '''
            Temporary method to insert articles into the database
        '''
        try:
            search_term = request.form.get('search_term')
            task_id = request.form.get('task_id')
            insert_articles(search_term, task_id)
            return dict(status='Articles successfully inserted.'), 201
        except Exception as e:
            abort(400, str(e))
