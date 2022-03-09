import functools
from flask import (
    Blueprint,  render_template, request, url_for
)

bp_news = Blueprint('news', __name__, url_prefix='/news',template_folder='templates')
print("name BP news ?? ", __name__) ## __name__ ---> app.news

from datetime import datetime
import feedparser 
from flask import render_template
from flask import request,session
import math

@bp_news.route('/lastnews', methods=['GET', 'POST'])
def news():
    
    if request.method == 'GET':
        ya ='http://news.yandex.ru/Russia/index.rss'
    
    if request.method == 'POST':
        form = request.form
        ya =f'http://news.yandex.ru/{form["search_text"]}/index.rss'
        
        # if form['search_text'] == 'Ukraine':
        #    ya='http://news.yandex.ru/Ukraine/index.rss'
        # else:    
        #    ya='http://news.yandex.ru/Russia/index.rss'
       
    # km='http://www.kommersant.ru/RSS/news.xml'
    
    cols =3
    data = feedparser.parse(ya)
    entr = data['entries']
      
    smallentr= entr[0:5]
    
    if len(smallentr) == 0:
        return render_template('404.html')
       
    return render_template(
        '/news/news.html',
        title='Новости',
        cols=cols,
        rows =math.ceil(len(smallentr)/cols),
        data=smallentr
    )
