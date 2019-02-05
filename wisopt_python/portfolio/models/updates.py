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


# Function to update the experience details for the user_id
def update_experience(user_id, experience_id, title, location, start_date, end_date, experience_desc, employer_name):
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
            emp_id = check_employer_existing(employer_name)
            if emp_id == -1:
                cur.execute(
                    "INSERT INTO table_employers (employer_name) VALUES (%s)", (employer_name))
                cur.execute(
                    "SELECT employer_id FROM table_employers WHERE employer_name=%s", (employer_name))
                emp_id_t = cur.fetchall()
                emp_id = emp_id_t[0]['employer_id']
            cur.execute(
                "UPDATE table_experience SET user_id = %s, title = %s, employer_id = %s, start_date = %s, end_date = %s, location = %s, experience_desc = %s WHERE experience_id = %s",
                (user_id, title, emp_id, start_date, end_date, location, experience_desc, experience_id))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')


# Function to update the extra curricular details for the user_id
def update_extra_curricular(user_id, ec_id, ec_type, ec_name, ec_desc, start_date, end_date):
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
            cur.execute("UPDATE table_extra_curricular SET user_id=%s, extra_curricular_type=%s, extra_curricular_name=%s, description=%s, start_date=%s, end_date=%s WHERE extra_curricular_id = %s",
                        (user_id, ec_type, ec_name, ec_desc, start_date, end_date, ec_id))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')
