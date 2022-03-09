from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app import db



bp = Blueprint('general', __name__, template_folder='templates')
print('name - general',__name__, __name__)

@bp.route('/')
@bp.route('/index')
def index():
    d=db.get_db()
    print("database ", d)
    return render_template(
    '/general2/index.html',
    title='Home Page',
       
    )