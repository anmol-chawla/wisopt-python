from flask import request, jsonify, abort
from flask_restplus import Resource, fields

from ..common.authenticate import verify_token
from .models.insertions import insert_education, insert_experience, insert_extra_curricular, insert_social
from .models.updates import update_education, update_experience, update_extra_curricular, update_social
from .. import portfolio_apis as api

api_parser = api.parser()
api_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')

insertEducation_fields = api.model('Education(insertion)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'start_year': fields.String(required=True, description='Start year of the particular education'),
    'end_year': fields.String(required=True, description='End year of the particular edcuation'),
    'education_name': fields.String(required=True, description='Name of the education entered'),
    'education_desc': fields.String(required=True, description='Description about the education'),
    'intitute_name': fields.String(required=True, description='Insititute from where the education was recieved')
}
)

updateEducation_fields = api.model('Education(updation)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'start_year': fields.String(required=True, description='Start year of the particular education'),
    'end_year': fields.String(required=True, description='End year of the particular edcuation'),
    'education_id': fields.Integer(required=True, description='ID of the education'),
    'education_name': fields.String(required=True, description='Name of the education entered'),
    'education_desc': fields.String(required=True, description='Description about the education'),
    'intitute_name': fields.String(required=True, description='Insititute from where the education was recieved')
}
)


class Education(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertEducation_fields, parser=api_parser)
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

    @api.doc(body=updateEducation_fields, parser=api_parser)
    @api.response(201, 'Education details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the education details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            start_year = request.form.get('start_year')
            end_year = request.form.get('end_year')
            education_id = request.form.get('education_id')
            education_name = request.form.get('education_name')
            education_desc = request.form.get('education_desc')
            institute_name = request.form.get('institute_name')
            update_education(user_id, education_id, start_year, end_year,
                             education_name, education_desc, institute_name)
            return dict(status='Education details successfully updated.'), 201
        except Exception as e:
            abort(400, str(e))


insertExperience_fields = api.model('Experience(insertion)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'start_date': fields.String(required=True, description='Start date of the particular experience'),
    'end_date': fields.String(required=True, description='End date of the particular experience'),
    'title': fields.String(required=True, description='Name of the experience entered'),
    'experience_desc': fields.String(required=True, description='Description about the experience'),
    'employer_name': fields.String(required=True, description='Name of employer under whom the experience was obtained'),
    'location': fields.String(required=True, description='Location from where the experience was obtained')
}
)

updateExperience_fields = api.model('Experience(updation)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'experience_id': fields.Integer(required=True, description='ID of the exprience'),
    'start_date': fields.String(required=True, description='Start date of the particular experience'),
    'end_date': fields.String(required=True, description='End date of the particular experience'),
    'title': fields.String(required=True, description='Name of the experience entered'),
    'experience_desc': fields.String(required=True, description='Description about the experience'),
    'employer_name': fields.String(required=True, description='Name of employer under whom the experience was obtained'),
    'location': fields.String(required=True, description='Location from where the experience was obtained')
}
)


class Experience(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertExperience_fields, parser=api_parser)
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

    @api.doc(body=updateExperience_fields, parser=api_parser)
    @api.response(201, 'Experience details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the experience details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            experience_id = request.form.get('experience_id')
            title = request.form.get('title')
            employer_name = request.form.get('employer_name')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            location = request.form.get('location')
            experience_desc = request.form.get('experience_desc')
            update_experience(user_id, experience_id, title, location, start_date,
                              end_date, experience_desc, employer_name)
            return dict(status='Experience details successfully updated.'), 201
        except Exception as e:
            abort(400, str(e))


insertExtraCurricular_fields = api.model('ExtraCurricular(insertion)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'start_date': fields.String(required=True, description='Start date of the particular extra curricular activity'),
    'end_date': fields.String(required=True, description='End date of the particular extra curricular activity'),
    'ec_name': fields.String(required=True, description='Possible fields - enum(Sports, Arts, Volunteering, Hobby, Other)'),
    'ec_desc': fields.String(required=True, description='Description about the extra curricular activity'),
    'ec_type': fields.String(required=True, description='Type of extra curricular activity'),
})

updateExtraCurricular_fields = api.model('ExtraCurricular(updation)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'ec_id': fields.Integer(required=True, description='ID of the extra curricular activity'),
    'start_date': fields.String(required=True, description='Start date of the particular extra curricular activity'),
    'end_date': fields.String(required=True, description='End date of the particular extra curricular activity'),
    'ec_name': fields.String(required=True, description='Possible fields - enum(Sports, Arts, Volunteering, Hobby, Other)'),
    'ec_desc': fields.String(required=True, description='Description about the extra curricular activity'),
    'ec_type': fields.String(required=True, description='Type of extra curricular activity'),
})


class ExtraCurricular(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertExtraCurricular_fields, parser=api_parser)
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

    @api.doc(body=updateExtraCurricular_fields, parser=api_parser)
    @api.response(201, 'Extra curricular details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the extra curricular details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            ec_id = request.form.get('ec_id')
            ec_type = request.form.get('ec_type')
            ec_name = request.form.get('ec_name')
            ec_desc = request.form.get('ec_desc')
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            update_extra_curricular(
                user_id, ec_id, ec_type, ec_name, ec_desc, start_date, end_date)
            return dict(status='Extra curricular details successfully updated.'), 201
        except Exception as e:
            abort(400, str(e))


insertSocial_fields = api.model('Social(insertion)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'social_name': fields.String(required=True, description='Name of the social activity entered'),
    'social_link': fields.String(required=True, description='Link of social activity'),
})

updateSocial_fields = api.model('Social(updation)', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'social_id': fields.Integer(required=True, description='User ID'),
    'social_name': fields.String(required=True, description='Name of the social activity entered'),
    'social_link': fields.String(required=True, description='Link of social activity'),
})

class Social(Resource):
    method_decorators = [verify_token]

    @api.doc(body=insertSocial_fields, parser=api_parser)
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

    @api.doc(body=updateSocial_fields, parser=api_parser)
    @api.response(201, 'Social details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the social details for the user_id
        """
        try:
            user_id = request.form.get('user_id')
            social_id = request.form.get('social_id')
            social_name = request.form.get('social_name')
            social_link = request.form.get('social_link')
            update_social(user_id, social_id, social_name, social_link)
            return dict(status='Social details successfully updated'), 201
        except Exception as e:
            abort(400, str(e))
