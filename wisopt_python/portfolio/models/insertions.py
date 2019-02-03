import pymysql
from flask import current_app
from .check import check_employer_existing
from ... import app


# Function to insert the education details for the provided user_id
def insert_education(user_id, start_year, end_year, education_name, education_desc, institute_name):
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
                "INSERT INTO table_education (student_id, institute_name, start_year, end_year, education_name, education_desc) VALUES (%s, %s, %s, %s, %s, %s)",
                (user_id, institute_name, start_year, end_year, education_name, education_desc))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')


# Function to insert experience details for the provided user_id
def insert_experience(user_id, title, location, start_date, end_date, experience_desc, employer_name):
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
                "INSERT INTO table_experience (user_id, title, employer_id, start_date, end_date, location, experience_desc) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (user_id, title, emp_id, start_date, end_date, location, experience_desc))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')


# Function to insert extra curricular activities for the provided user_id
def insert_extra_curricular(user_id, ec_type, ec_name, ec_desc, start_date, end_date):
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
            cur.execute("INSERT INTO table_extra_curricular (user_id, extra_curricular_type, extra_curricular_name, description, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)",
                        (user_id, ec_type, ec_name, ec_desc, start_date, end_date))
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')
