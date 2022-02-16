from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from logging.config import dictConfig
from logging.handlers import WatchedFileHandler

from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)

hnd = WatchedFileHandler('logger.log')
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s -in- %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



app.debug = True
app.logger.addHandler(hnd)
app.logger.debug('A value for debugging')


app.config['SECRET_KEY'] = '123456789'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
app.config['CORS_HEADERS'] = 'Content-Type'

# print(app.config)
toolbar = DebugToolbarExtension(app)

from app import routes
from app import special