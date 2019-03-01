import pymysql
import random
from flask import current_app
from ... import app
from googleapiclient.discovery import build
from .insertions import insert_articles
try:
    from .insertions import normalize
except ImportError:
    pass


# Get articles for insertion into the database
def fetch_articles(search_term):
    try:
        with app.app_context():
            api_key = current_app.config['GOOGLE_API_KEY']
            cse_id = current_app.config['GOOGLE_CSE_ID']
        results = []
        searches = []
        search_term = normalize(search_term)
        templates = ['tips', 'best practices', 'tutorial',
                     'examples', 'tricks', 'common mistakes']
        for i in templates:
            searches.append(search_term + str(" ") + i)
        service = build("customsearch", "v1", developerKey=api_key)
        for query in searches:
            res = service.cse().list(q=query, cx=cse_id,
                                     num=5, filter='1').execute()['items']
            for i in res:
                r1 = {}
                r1['query'] = query
                r1['content_link'] = i['link']
                r1['content_title'] = i['title']
                r1['content_provider'] = i['displayLink']
                r1['content_description'] = i['snippet'].replace('\n', '')
                results.append(r1)
        return results
    except Exception:
        raise Exception('Unable to connect to server database')


# Get articles for the user
def return_articles(search_term, task_id):
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
    cur.execute("SELECT content_title, content_link, content_description, content_type, search_term, task_id FROM table_goals_content WHERE search_term=%s", (search_term))
    content = cur.fetchall()
    if(len(content) < 5):
        insert_articles(search_term, task_id)
    try:
        posns = random.sample(range(0, len(content)), 5)
    except Exception:
        return "Cannot currently find relevant articles for this topic. Sorry for the inconvenience"
    articledata = []
    for i in posns:
        articledata.append(content[i])
    con.close()
    return articledata
