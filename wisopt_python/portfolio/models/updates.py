import pymysql
from flask import current_app
from .check import check_employer_existing
from ... import app


# Function to update education details for the user_id
def update_education(user_id, education_id, start_year, end_year, education_name, education_desc, institute_name):
    try:
        with app.app_context():
            con = pymysql.connect(host=current_app.config['DB_HOST'],
                                  user=current_app.config['DB_USER'],
                                  password=current_app.config['DB_PASSWORD'],
                                  db=current_app.config['DB'],
                                  charset=current_app.config['DB_CHARSET'],
                                  cursorclass=pymysql.cursors.DictCursor,
                                  port=current_app.config['DB_PORT'])
            cur = con.cursor()
            cur.execute(
                "UPDATE table_education SET student_id = %s, institute_name = %s, start_year = %s, end_year = %s, education_name = %s, education_desc = %s WHERE education_id=%s",
                (user_id, institute_name, start_year, end_year, education_name, education_desc, education_id))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')
