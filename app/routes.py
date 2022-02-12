from app import app
from datetime import datetime
from flask import render_template
from flask import request
from markupsafe import escape

#Экранирование!!!
@app.route('/<name>')
def safe(name):
    return f"Привет {escape(name)}!"
#subpath
@app.route('/path/<path:somepath>')
def pth(somepath):
    return f'Somepath {escape(somepath)}'
#float
@app.route('/float/<float:idn>')
def flt(idn):
    return f'number: {isinstance(idn,float)} - {idn}'

#multi
@app.route('/mult/<one>/<two>')
def mlt(one=None, two=999):
    return  f'result {one}=={two}'
    #safe('ccc') #

#args  /args?one=qwer&two=asd&three=zxc
@app.route('/args/<string:one>')
def arg(*args):
    var1  = request.args.get('one', None)
    var2  = request.args.get('two', None)
    var3  = request.args.get('three', None)
    return f'<html><body>{var1} {var2} {var3}</body></html>'



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