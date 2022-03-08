import functools

from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('third', __name__, url_prefix='/third',template_folder='templates')
print("name BP third ?? ", __name__) ##__name__  app.rts.lnk

@bp.route('/mylink')
def about():
  return render_template(  
        'rts/about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')