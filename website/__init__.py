
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import requests
from flask_migrate import Migrate 
from .models import db
import flask_sqlalchemy

migrate = Migrate()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY']= '7997'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 
    db.init_app(app)
    migrate.init_app(app, db)


    from .pages import pages
    from.auth import auth
    
    app.register_blueprint(pages, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
  

    from .models import User
    from .models import LearnedWord
    with app.app_context():
        db.create_all()
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
