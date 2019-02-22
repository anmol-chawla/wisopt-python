import pymysql
from flask import current_app
from ... import app


# Fetch the promotion events
def promotion_events():
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
    except Exception as e:
        raise Exception('Unable to connect to server database')
    cur.execute('SELECT * FROM table_event WHERE is_promotion="true"')
    events = cur.fetchall()
    return events
