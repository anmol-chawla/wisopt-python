from flask import request, abort, jsonify
from flask_restplus import Resource

from ..common.authenticate import verify_token
from .models.fetch import return_articles
from .models.insertions import insert_articles
from .. import base_parser, api


# Declaring a parser object for fetching articles
fetchArticle_parser = base_parser.copy()
fetchArticle_parser.add_argument(
    'search_term', type=str, location='args', required=True, help='The term for which articles need to be fetched')
fetchArticle_parser.add_argument(
    'task_id', type=int, location='args', required=True, help='Task ID')

# Declaring a parser object for inserting articles
insertArticle_parser = base_parser.copy()
insertArticle_parser.add_argument(
    'search_term', type=str, location='args', required=True, help='The term for which articles need to be fetched')
insertArticle_parser.add_argument(
    'task_id', type=int, location='args', required=True, help='Task ID')


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
            task_id = request.args.get('task_id')
            data = return_articles(search_term, task_id)
            return jsonify(data)
        except Exception as e:
            abort(400, str(e))

    @api.doc(parser=insertArticle_parser)
    @api.response(201, 'Articles successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        '''
            Temporary method to insert articles into the database
        '''
        try:
            search_term = request.args.get('search_term')
            task_id = request.args.get('task_id')
            insert_articles(search_term, task_id)
            return dict(status='Articles successfully inserted.'), 201
        except Exception as e:
            abort(400, str(e))
