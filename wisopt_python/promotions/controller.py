from flask import abort, jsonify
from flask_restplus import Resource

from ..common.authenticate import verify_token
from .models.fetch import promotion_events
from .. import promotions_apis as api


# Declaring a base parser object with the arguments required for each route
base_parser = api.parser()
base_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')
base_parser.add_argument(
    'user_id', type=int, location='headers', required=True, help='User ID')


class Promotions(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=base_parser)
    @api.response(201, 'JSON response')
    @api.response(401, 'Unauthorized access')
    def get(self):
        '''
            Method to get the current promotions
        '''
        try:
            return jsonify(promotion_events())
        except Exception as e:
            abort(400, str(e))
