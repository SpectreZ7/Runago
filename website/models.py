
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    Username = db.Column(db.String(150))
    learnedwords = db.relationship('LearnedWord', lazy = True)
    library = db.Column(db.String(100))

class LearnedWord(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='learned_words') 
    word = db.Column(db.String(20), nullable=False)
    definition = db.Column(db.String(50), nullable=True)
    




