from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
print('app? ', app)
app.config['SECRET_KEY'] = '123456789'
# print(app.config)
toolbar = DebugToolbarExtension(app)

from app import routes
from app import special