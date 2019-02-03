import pymysql

from functools import wraps
from flask import request, current_app, abort
from ... import app


# Function to check if the request is coming from a registered account
def verify_token(f):
    @wraps(f)
    def func_wrapper(**kwargs):
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
                token = request.headers.get('token')
                reg_id = request.form.get('user_id')
                if token and reg_id:
                    sql = "SELECT token_code FROM users WHERE token_code=\"" + \
                          token + "\" and user_id=" + reg_id + ";"
                    cur.execute(sql)
                    data = cur.fetchall()
                    if len(data) == 0:
                        abort(401, 'Unauthorized access')
                    else:
                        abort(400, 'Missing token')
            return f(**kwargs)
        except Exception as e:
            return dict(status='error', error=str(e)), 400
    return func_wrapper


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
