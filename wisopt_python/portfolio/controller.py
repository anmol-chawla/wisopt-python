from flask import request, abort
from flask_restplus import Resource

from ..common.authenticate import verify_token
from .models.insertions import insert_education, insert_experience, insert_extra_curricular, insert_social
from .models.updates import update_education, update_experience, update_extra_curricular, update_social
from .models.deletions import delete_education, delete_experience, delete_extra_curricular, delete_social
from .. import portfolio_apis as api

# Declaring a base parser object with the arguments required for each route
base_parser = api.parser()
base_parser.add_argument(
    'token', location='headers', required=True, help='Token for the given user id')
base_parser.add_argument(
    'user_id', type=int, location='headers', required=True, help='User ID')

# Declaring a parser object for inserting data with the necessary arguments
insertEducation_parser = base_parser.copy()
insertEducation_parser.add_argument(
    'start_year', type=str, location='form', required=True, help='Start year of the particular education')
insertEducation_parser.add_argument(
    'end_year', type=str, location='form', required=False, help='End year of the particular education')
insertEducation_parser.add_argument(
    'education_name', type=str, location='form', required=True, help='Name of the education entered')
insertEducation_parser.add_argument(
    'education_desc', type=str, location='form', required=True, help='Description about the education')
insertEducation_parser.add_argument(
    'institute_name', type=str, location='form', required=True, help='Insititute from where the education was recieved')

# Creating a copy of the insertion parser and adding an argument for the id of the resource in the db
updateEducation_parser = insertEducation_parser.copy()
updateEducation_parser.add_argument(
    'education_id', type=int, location='form', required=True, help='ID of the education')

# Declaring a deletetion parser object for the delete the resource at the id in the db
deleteEducation_parser = base_parser.copy()
deleteEducation_parser.add_argument(
    'education_id', type=int, location='form', required=True, help='ID of the education')


class Education(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=insertEducation_parser)
    @api.response(201, 'Education details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the education details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=updateEducation_parser)
    @api.response(200, 'Education details successfully deleted.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the education details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=deleteEducation_parser)
    @api.response(201, 'Education details successfully deleted.')
    @api.response(401, 'Unauthorized access')
    def delete(self):
        """
            Delete the education detail for education_id
        """
        try:
            education_id = request.form.get('education_id')
            delete_education(education_id)
            return dict(status='Education details successfully deleted.'), 200
        except Exception as e:
            abort(400, str(e))


# Declaring a parser object for inserting data with the necessary arguments
insertExperience_parser = base_parser.copy()
insertExperience_parser.add_argument(
    'start_date', type=str, location='form', required=True, help='Start date of the particular experience')
insertExperience_parser.add_argument(
    'end_date', type=str, location='form', required=False, help='End date of the particular experience')
insertExperience_parser.add_argument(
    'title', type=str, location='form', required=True, help='Title of the experience entered')
insertExperience_parser.add_argument(
    'experience_desc', type=str, location='form', required=True, help='Description about the experience')
insertExperience_parser.add_argument(
    'employer_name', type=str, location='form', required=True, help='Name of employer under whom the experience was obtained')
insertExperience_parser.add_argument(
    'location', type=str, location='form', required=True, help='Location from where the experience was obtained')

# Creating a copy of the insertion parser and adding an argument for the id of the resource in the db
updateExperience_parser = insertExperience_parser.copy()
updateExperience_parser.add_argument(
    'experience_id', type=int, location='form', required=True, help='ID of the experience')

# Declaring a deletetion parser object for the delete the resource at the id in the db
deleteExperience_parser = base_parser.copy()
deleteExperience_parser.add_argument(
    'experience_id', type=int, location='form', required=True, help='ID of the experience')


class Experience(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=insertExperience_parser)
    @api.response(201, 'Experience details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the experience details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=updateExperience_parser)
    @api.response(201, 'Experience details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the experience details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=deleteExperience_parser)
    @api.response(200, 'Experience details successfully deleted.')
    @api.response(401, 'Unauthorized access')
    def delete(self):
        """
            Delete the experience details for the experience_id
        """
        try:
            experience_id = request.form.get('experience_id')
            delete_experience(experience_id)
            return dict(status='Experience details successfully deleted.'), 200
        except Exception as e:
            abort(400, str(e))


# Declaring a parser object for inserting data with the necessary arguments
insertExtraCurricular_parser = base_parser.copy()
insertExtraCurricular_parser.add_argument(
    'start_date', type=str, location='form', required=True, help='Start date of the particular extra curricular activity')
insertExtraCurricular_parser.add_argument(
    'end_date', type=str, location='form', required=False, help='End date of the particular extra curricular activity')
insertExtraCurricular_parser.add_argument(
    'ec_name', type=str, location='form', required=True, help='Title of the extra curricular activity entered')
insertExtraCurricular_parser.add_argument(
    'ec_desc', type=str, location='form', required=True, help='Description about the extra curricular activity')
insertExtraCurricular_parser.add_argument(
    'ec_type', type=str, location='form', required=True, help='Name of employer under whom the experience was obtained')
insertExtraCurricular_parser.add_argument(
    'location', type=str, location='form', required=True, help='Type of extra curricular activity')

# Creating a copy of the insertion parser and adding an argument for the id of the resource in the db
updateExtraCurricular_parser = insertExtraCurricular_parser.copy()
updateExtraCurricular_parser.add_argument(
    'ec_id', type=int, location='form', required=True, help='ID of the extra curricular activity')

# Declaring a deletetion parser object for the delete the resource at the id in the db
deleteExtraCurricular_parser = base_parser.copy()
deleteExtraCurricular_parser.add_argument(
    'ec_id', type=int, location='form', required=True, help='ID of the extra curricular activity')


class ExtraCurricular(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=insertExtraCurricular_parser)
    @api.response(201, 'Extra curricular details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the extra curriculara details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=updateExtraCurricular_parser)
    @api.response(201, 'Extra curricular details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the extra curricular details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
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

    @api.doc(parser=deleteExtraCurricular_parser)
    @api.response(200, 'Extra curricular details successfully deleted.')
    @api.response(401, 'Unauthorized access')
    def delete(self):
        """
            Delete the extra curricular details for the given ec_id
        """
        try:
            ec_id = request.form.get('ec_id')
            delete_extra_curricular(ec_id)
            return dict(status='Extra curricular details successfully deleted.'), 200
        except Exception as e:
            abort(400, str(e))


# Declaring a parser object for inserting data with the necessary arguments
insertSocial_parser = base_parser.copy()
insertSocial_parser.add_argument(
    'social_name', type=str, location='form', required=True, help='Name of the social activity entered')
insertSocial_parser.add_argument(
    'social_link', type=str, location='form', required=True, help='Link of social activity')

# Creating a copy of the insertion parser and adding an argument for the id of the resource in the db
updateSocial_parser = insertSocial_parser.copy()
updateSocial_parser.add_argument(
    'social_id', type=int, location='form', required=True, help='ID of the social detail')

# Declaring a deletetion parser object for the delete the resource at the id in the db
deleteSocial_parser = base_parser.copy()
deleteSocial_parser.add_argument(
    'social_id', type=int, location='form', required=True, help='ID of the social detail')


class Social(Resource):
    method_decorators = [verify_token]

    @api.doc(parser=insertSocial_parser)
    @api.response(201, 'Social details successfully inserted.')
    @api.response(401, 'Unauthorized access')
    def post(self):
        """
            Insert the social details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
            social_name = request.form.get('social_name')
            social_link = request.form.get('social_link')
            insert_social(user_id, social_name, social_link)
            return dict(status='Social details successfully inserted'), 201
        except Exception as e:
            abort(400, str(e))

    @api.doc(parser=updateSocial_parser)
    @api.response(201, 'Social details successfully updated.')
    @api.response(401, 'Unauthorized access')
    def put(self):
        """
            Update the social details for the user_id
        """
        try:
            user_id = request.headers.get('user_id')
            social_id = request.form.get('social_id')
            social_name = request.form.get('social_name')
            social_link = request.form.get('social_link')
            update_social(user_id, social_id, social_name, social_link)
            return dict(status='Social details successfully updated'), 201
        except Exception as e:
            abort(400, str(e))

    @api.doc(parser=deleteSocial_parser)
    @api.response(200, 'Social details successfully deleted.')
    @api.response(401, 'Unauthorized access')
    def delete(self):
        """
            Delete the social details for the social_id
        """
        try:
            social_id = request.form.get('social_id')
            delete_social(social_id)
            return dict(status='Social details successfully deleted'), 200
        except Exception as e:
            abort(400, str(e))
