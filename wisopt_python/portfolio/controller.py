from flask import request, jsonify, abort
from flask_restplus import Resource, fields

from .models.check import verify_token
from .models.insertions import insert_education, insert_experience
from .. import portfolio_apis as api


insertEducation_fields = api.model('insertEducation', {
    'user_id': fields.String(required=True, description='User ID'),
    'start_year': fields.String(required=True, description='Start year of the particular education'),
    'end_year': fields.String(required=True, description='End year of the particular edcuation'),
    'education_name': fields.String(required=True, description='Name of the education entered'),
    'education_desc': fields.String(required=True, description='Description about the education'),
    'intitute_name': fields.String(required=True, description='Insititute from where the education was recieved')
}
)
insert_education_parser = api.parser()
insert_education_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class insertEducation(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertEducation_fields, parser=insert_education_parser)
    @api.response(201, 'Education details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the education details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            start_year = request.form.get('start_year')
            end_year = request.form.get('end_year')
            education_name = request.form.get('education_name')
            education_desc = request.form.get('education_desc')
            institute_name = request.form.get('institute_name')
            insert_education(user_id, start_year, end_year,
                             education_name, education_desc, institute_name)
            return dict(status='Education details successfully inserted.'), 201
        except Exception as e:
            abort(400, str(e))


insertExperience_fields = api.model('insertExperience', {
    'user_id': fields.String(required=True, description='User ID'),
    'start_date': fields.String(required=True, description='Start date of the particular experience'),
    'end_date': fields.String(required=True, description='End date of the particular experience'),
    'title': fields.String(required=True, description='Name of the experience entered'),
    'experience_desc': fields.String(required=True, description='Description about the experience'),
    'employer_name': fields.String(required=True, description='Name of employer under whom the experience was obtained'),
    'location': fields.String(required=True, description='Location from where the experience was obtained')
}
)
insert_experience_parser = api.parser()
insert_experience_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class insertExperience(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertExperience_fields, parser=insert_experience_parser)
    @api.response(201, 'Experience details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the experience details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            title = request.form.get('title')
            employer_name = request.form.get('employer_name')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            location = request.form.get('location')
            experience_desc = request.form.get('experience_desc')
            insert_experience(user_id, title, location, start_date,
                              end_date, experience_desc, employer_name)
            return dict(status='Experience details successfully inserted.'), 201
        except Exception as e:
            abort(400, str(e))
