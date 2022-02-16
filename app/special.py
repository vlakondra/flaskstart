from app import app
from flask import render_template, redirect,url_for
from flask_cors import CORS, cross_origin
from app.forms import LoginForm

@app.route('/special/simple/<string:name>')
def Safe(name):
    return f"Привет {name}!!!!!!"


# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Вход', form=form)    

@app.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index',_external=True,_scheme='https'))
    return render_template('login.html', title='Sign In', form=form)