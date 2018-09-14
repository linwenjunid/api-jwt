from flask import Flask,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT,jwt_required
from flask_restplus import Api,Resource

db = SQLAlchemy()
conf = Config()

def create_app():
    app=Flask(__name__)
    app.config.from_object(conf)

    #@app.after_request
    #def after_request(response):
    #    response.headers.add('Access-Control-Allow-Origin', '*')
    #    if request.method == 'OPTIONS':
    #        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
    #        headers = request.headers.get('Access-Control-Request-Headers')
    #        if headers:
    #            response.headers['Access-Control-Allow-Headers'] = headers
    #    return response
    
    conf.init_app(app)
    db.init_app(app)

    from app.auth.jwt import authenticate,identity
    jwt = JWT(app, authenticate, identity)

    from .plus import plus as plus_blueprint
    app.register_blueprint(plus_blueprint,url_prefix='/plus')

    from .v1_0 import api as v1_0_blueprint
    app.register_blueprint(v1_0_blueprint,url_prefix='/api')

    return app
