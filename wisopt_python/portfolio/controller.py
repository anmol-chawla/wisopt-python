from flask import request, jsonify
from flask_restful import Resource

from .models.check import verify_token
from .models.insertions import insert_education


class insertEducation(Resource):
    # Class to insert education for the user_id. Requires a POST call to the end point
    method_decorators = [verify_token]

    def post(self):
        try:
            user_id = request.form.get('user_id')
            start_year = request.form.get('start_year')
            end_year = request.form.get('end_year')
            education_name = request.form.get('education_name')
            education_desc = request.form.get('education_desc')
            institute_name = request.form.get('institute_name')
            insert_education(user_id, start_year, end_year,
                             education_name, education_desc, institute_name)
            return jsonify(dict(status='Success'))
        except Exception as e:
            return jsonify(dict(status='error', error=str(e)))
