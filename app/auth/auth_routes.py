import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth',template_folder="templates")

@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Введите имя пользователя'
        elif not password:
            error = 'Введите пароль'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Пользователь {username} уже зарегистрирован."
            else:
                # return redirect(url_for("auth.login",_external=True, _scheme='https'))
                return redirect(request.origin+"/auth/login")
        flash(error)
        
    return render_template(
        '/auth/register.html',
        title='Регистрация',)


@bp_auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Неправильное имя пользователя.'
        elif not check_password_hash(user['password'], password):
            error = 'Неправильный пароль.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            # return redirect(url_for('general.index'))
            return redirect(request.origin+url_for('general.index'))

        flash(error)
    return render_template(
        '/auth/login.html',
        title='Вход',)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # return redirect(url_for('auth.login'))
            return redirect(request.referrer.split('/')[0] + url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp_auth.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    # return redirect(request.origin + url_for('general.index'))
    # return render_template('/general/index.html')
    return redirect(request.referrer.split('/')[0] + url_for('general.index'))
    


@bp_auth.before_app_request
def load_logged_in_user():
    
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
        
   
        