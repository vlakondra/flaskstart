import functools

from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('second', __name__, url_prefix='/second')


@bp.route('/about')
def about():
  return render_template(  
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')
