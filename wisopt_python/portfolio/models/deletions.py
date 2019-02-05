import pymysql
from flask import current_app
from .check import check_employer_existing
from ... import app


# Function to delete the given education_id
def delete_education(education_id):
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
                "DELETE FROM table_education WHERE education_id = %s",education_id)
            con.commit()
            con.close()
    except Exception as e:
        raise Exception('Unable to connect to server database')
