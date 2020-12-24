import os
from os.path import join, dirname
from flask import Flask
from dotenv import load_dotenv
#load_dotenv()   
dotenv_path = join(dirname(__file__), 'structure.env')
load_dotenv(dotenv_path)


"""
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print("OS environ after", os.environ['APP_SETTINGS'])
if __name__ == '__main__':
    app.run()
    print(os.environ['APP_SETTINGS'])exit()
"""

def create_app(test_config = None):
    os.environ.get('FLASK_APP')
    os.environ.get('FLASK_ENV')
    # create and configure the app
    #print(os.environ['FLASK_APP'])
    #print(os.environ['FLASK_ENV'])
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )





    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load the test config if passed in 
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app

if __name__ == '__main__':
    create_app()