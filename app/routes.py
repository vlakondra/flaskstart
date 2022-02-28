from app import app
from datetime import datetime
import feedparser 
from flask import render_template
from flask import request,session
from markupsafe import escape
import math



@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/news', methods=['GET', 'POST'])
def news():
    
    if request.method == 'GET':
        ya ='http://news.yandex.ru/Russia/index.rss'
    
    if request.method == 'POST':
        form = (request.form)
        ya =f'http://news.yandex.ru/{form["search_text"]}/index.rss'
        
        # if form['search_text'] == 'Ukraine':
        #    ya='http://news.yandex.ru/Ukraine/index.rss'
        # else:    
        #    ya='http://news.yandex.ru/Russia/index.rss'
       
    # km='http://www.kommersant.ru/RSS/news.xml'
    
    cols =3
    data = feedparser.parse(ya)
    entr = data['entries']
      
    smallentr= entr[0:4]
    
    if len(smallentr) == 0:
        return render_template('404.html')
       
    return render_template(
        'news.html',
        title='Новости',
        cols=cols,
        rows =math.ceil(len(smallentr)/cols),
        data=smallentr
    )


@app.route('/about')
def about():
  return render_template(  
        'about.html',
        title='About',
         username=session['username'],
        year=datetime.now().year,
        message='Your application description page.')

#https://jinja.palletsprojects.com/en/3.0.x/templates/#jinja-filters.length
# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3-ru
@app.route('/contact')
def contact():
 app.logger.debug("???")   
 var1  = session['username']
 app.logger.debug(var1) 

 return render_template(
        'contact.html',
        word= "Hello world!",
        username=session['username'],
        title='Contact',
        year=datetime.now().year,
        message='Моя contact page.'
    )