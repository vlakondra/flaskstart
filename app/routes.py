from app import app
from datetime import datetime
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


# def index():
#     user = {'username': 'Miguel'}
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''


@app.route('/about')
def about():
  return render_template(  
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')


@app.route('/contact')
def contact():
 return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Моя contact page.'
    )