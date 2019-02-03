import pymysql

from functools import wraps
from flask import jsonify, request, current_app
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
                    return jsonify(dict(status='error', error='Unauthorized access'))
            else:
                return jsonify(dict(status='error', error='Missing token'))
        return f(**kwargs)
      except Exception as e:
        return jsonify(dict(status='error', error=str(e)))
    return func_wrapper
