from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask import redirect,url_for
from app import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    email=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    member_since=db.Column(db.DateTime(),default=datetime.utcnow)
    last_seen=db.Column(db.DateTime(),default=datetime.utcnow)
    head_img = db.Column(db.Unicode(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribut')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def ping(self):
        self.last_seen=datetime.utcnow()
        db.session.add(self)

    def can(self,permissions):
        return True

    def is_administrator(self):
        return True

