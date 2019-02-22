import pymysql

from flask import current_app
from ... import app


# Function to check for duplicate entries
def check_duplicates(article_link):
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
        sql = "SELECT content_id FROM table_goals_content WHERE content_link=" + \
              '"' + article_link + '"'
        cur.execute(sql)
        data = cur.fetchall()
        if len(data) == 0:
            return False
        else:
            return True

    except Exception:
        raise Exception('Unable to connect to server database')
