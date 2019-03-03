from flask import request, abort, jsonify
from flask_restplus import Resource

from ..common.authenticate import verify_token
from .models.fetch import return_articles
from .models.insertions import rate_content
from .. import base_parser, api


# Declaring a parser object for fetching articles
fetchArticle_parser = base_parser.copy()
fetchArticle_parser.add_argument(
    'search_term', type=str, location='args', required=True, help='The term for which articles need to be fetched')
fetchArticle_parser.add_argument(
    'task_id', type=int, location='args', required=True, help='Task ID')


# Declaring a parser object for article feedback
rateArticle_parser = base_parser.copy()
rateArticle_parser.add_argument(
    'content_id', type=int, location='args', required=True, help='The id for content to be rated')
rateArticle_parser.add_argument(
    'score', type=int, location='args', required=True, help='Score (1 or -1 or -3)')


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

    @api.doc(parser=rateArticle_parser)
    @api.response(201, 'Article successfully rated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        '''
            Method to rate articles and insert into database
        '''
        try:
            score = request.args.get('score')
            content_id = request.args.get('content_id')
            rate_content(content_id, score)
            return dict(status='Articles successfully rated.'), 201
        except Exception as e:
            abort(400, str(e))
