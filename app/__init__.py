from flask import Flask
import os
from flask_debugtoolbar import DebugToolbarExtension
from flask import  session, request


# app = Flask(__name__, template_folder='bulma')
# app.debug=True

# app.config['SECRET_KEY'] = '123456789'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
# app.config['CORS_HEADERS'] = 'Content-Type'

# toolbar = DebugToolbarExtension(app)


# from . import db
# from app import routes
# from app import special
def create_app(test_config=None):
    print('create_APP')
    app = Flask(__name__, 
                instance_relative_config=True, 
                template_folder='bulma')
    
    app.config.from_mapping(
        SECRET_KEY='123456789')
    
    toolbar = DebugToolbarExtension(app)
    
    from . import routes,links
    from app.rts  import lnk
    
    app.register_blueprint(routes.bp)
    app.register_blueprint(links.bp)
    
    app.register_blueprint(lnk.bp,options={'template_folder':'templ'})
    
    @app.route('/hello')
    def hello():
        return '<body>Hello, World!</body>'
    
    
    return app