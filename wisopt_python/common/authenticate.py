import pymysql

from functools import wraps
from flask import request, current_app, abort
from .. import app


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
                reg_id = request.headers.get('userid')
                if token and reg_id:
                    sql = "SELECT token_code FROM users WHERE token_code=\"" + \
                          token + "\" and user_id=" + reg_id + ";"
                    cur.execute(sql)
                    data = cur.fetchall()
                    if len(data) == 0:
                        abort(401, 'Unauthorized access')
                else:
                    abort(400, description='Missing token')
            return f(**kwargs)
        except Exception as e:
            return dict(status='error', error=str(e)), 400
    return func_wrapper
