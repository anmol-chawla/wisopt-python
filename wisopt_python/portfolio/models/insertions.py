import pymysql
from flask import current_app
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
