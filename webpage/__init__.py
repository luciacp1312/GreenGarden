from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # it's used to manage all the login parameters
from os import path

# Initialize the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_web():
    web = Flask(__name__) # To initialize Flask in the app
    web.config['SECRET_KEY'] = 't83 Gr3eN g4rD3n' #it's going to encrypt the cookies and session data related to our website
    web.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Specifying where the database is located
    db.init_app(web)

    # importing the files that use blueprints, and then we register them
    from .views import views
    from .auth import auth

    web.register_blueprint(views, url_prefix='/')
    web.register_blueprint(auth, url_prefix='/')

    from .database import User
    
    with web.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where to go if we are not logged in
    login_manager.init_app(web)

    @login_manager.user_loader
    def loadUser(id):
        return User.query.get(int(id))

    return web


# It checks if the db is already created. Otherwise, it will create it
def create_database(web):
    if not path.exists('webpage/' + DB_NAME):
        db.create_all(web=web)
        print('OK')
