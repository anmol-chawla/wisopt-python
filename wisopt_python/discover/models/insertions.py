import pymysql

from flask import current_app
from ... import app
from .check import check_duplicates
from .fetch import fetch_articles


def insert_articles(search_term, task_id):
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
    articles = fetch_articles(search_term)
    for article in articles:
        if not check_duplicates(article['content_link']):
            cur.execute(
                "INSERT INTO table_goals_content (task_id, search_term, content_title, content_description, content_link, content_provider, content_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (task_id, search_term, article['content_title'], article['content_description'], article['content_link'], article['content_provider'], "article"))
    con.commit()
    con.close()
