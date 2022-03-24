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
    app = Flask(__name__, 
                instance_relative_config=True, 
                template_folder='bulma')
    
    app.config.from_mapping(
        SECRET_KEY='123456789',
        DATABASE=os.path.join(app.instance_path, 'database.db'),
        COUNTRY='Russia',
        DEBUG_TB_INTERCEPT_REDIRECTS = False
    )
    
    print("DB? ",os.path.join(app.instance_path, 'database.db'))

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    toolbar = DebugToolbarExtension(app)
    
    from app import db
        
    from app.general import gen_routes
    from app.news import news_routes
    from app.auth import auth_routes
    from app.blog import blog_routes
  
    from app.icons import icons
        
    app.register_blueprint(gen_routes.bp_gen)
    app.register_blueprint(news_routes.bp_news)
    app.register_blueprint(auth_routes.bp_auth)
    app.register_blueprint(icons.icons_bp)
    app.register_blueprint(blog_routes.bp_blog)

    db.init_app(app)
    
    @app.route('/hello')
    def hello():
        return '<body>Тестовый маршрут!</body>'
    
    return app