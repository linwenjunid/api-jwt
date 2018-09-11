from app.models import User
from flask import current_app as app

def authenticate(username, password):
    user=User.query.filter(username==username).first()
    if user and user.verify_password(password):
        app.logger.info('认证:%s'%user.username)
        return user

def identity(payload):
    user_id = payload['identity']
    user=User.query.filter(User.id==user_id).first()
    if user:
        app.logger.info('确权:%s'%user.username)
        return user

