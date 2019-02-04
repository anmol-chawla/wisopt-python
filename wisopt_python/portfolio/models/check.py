import pymysql

from flask import current_app
from ... import app


# Function to check if the employer exists
def check_employer_existing(employer_name):
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
            try:
                cur.execute(
                    "SELECT employer_id FROM table_employers WHERE employer_name=%s", (employer_name))
                emp_id_t = cur.fetchall()
                emp_id = emp_id_t[0]['employer_id']
                return emp_id
            except Exception:
                return -1
    except Exception as e:
        raise Exception('Unable to connect to server database')
