from flask import request, jsonify, abort
from flask_restplus import Resource, fields

from ..common.authenticate import verify_token
from .models.insertions import insert_education, insert_experience, insert_extra_curricular, insert_social
from .. import portfolio_apis as api


Education_fields = api.model('Education', {
    'user_id': fields.String(required=True, description='User ID'),
    'start_year': fields.String(required=True, description='Start year of the particular education'),
    'end_year': fields.String(required=True, description='End year of the particular edcuation'),
    'education_name': fields.String(required=True, description='Name of the education entered'),
    'education_desc': fields.String(required=True, description='Description about the education'),
    'intitute_name': fields.String(required=True, description='Insititute from where the education was recieved')
}
)
education_parser = api.parser()
education_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class Education(Resource):
    method_decorators = [verify_token]

    @api.doc(body=Education_fields, parser=education_parser)
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


Experience_fields = api.model('Experience', {
    'user_id': fields.String(required=True, description='User ID'),
    'start_date': fields.String(required=True, description='Start date of the particular experience'),
    'end_date': fields.String(required=True, description='End date of the particular experience'),
    'title': fields.String(required=True, description='Name of the experience entered'),
    'experience_desc': fields.String(required=True, description='Description about the experience'),
    'employer_name': fields.String(required=True, description='Name of employer under whom the experience was obtained'),
    'location': fields.String(required=True, description='Location from where the experience was obtained')
}
)
experience_parser = api.parser()
experience_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class Experience(Resource):
    method_decorators = [verify_token]

    @api.doc(body=Experience_fields, parser=experience_parser)
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


ExtraCurricular_fields = api.model('ExtraCurricular', {
    'user_id': fields.String(required=True, description='User ID'),
    'start_date': fields.String(required=True, description='Start date of the particular extra curricular activity'),
    'end_date': fields.String(required=True, description='End date of the particular extra curricular activity'),
    'ec_name': fields.String(required=True, description='Name of the extra curricular activity entered'),
    'ec_desc': fields.String(required=True, description='Description about the extra curricular activity'),
    'ec_type': fields.String(required=True, description='Type of extra curricular activity'),
})
ec_parser = api.parser()
ec_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class ExtraCurricular(Resource):
    method_decorators = [verify_token]

    @api.doc(body=ExtraCurricular_fields, parser=ec_parser)
    @api.response(201, 'Extra curricular details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the extra curriculara details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            ec_type = request.form.get('ec_type')
            ec_name = request.form.get('ec_name')
            ec_desc = request.form.get('ec_desc')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            insert_extra_curricular(
                user_id, ec_type, ec_name, ec_desc, start_date, end_date)
            return dict(status='Extra curricular details successfully inserted.'), 201
        except Exception as e:
            abort(400, str(e))


Social_fields = api.model('Social', {
    'user_id': fields.String(required=True, description='User ID'),
    'social_name': fields.String(required=True, description='Name of the social activity entered'),
    'social_link': fields.String(required=True, description='Link of social activity'),
})
social_parser = api.parser()
social_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')


class Social(Resource):
    method_decorators = [verify_token]

    @api.doc(body=Social_fields, parser=social_parser)
    @api.response(201, 'Social details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the social details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            social_name = request.form.get('social_name')
            social_link = request.form.get('social_link')
            insert_social(user_id, social_name, social_link)
            return dict(status='Social details successfully inserted'), 201
        except Exception as e:
            abort(400, str(e))
