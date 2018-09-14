from flask import Blueprint,jsonify
from flask_jwt import jwt_required, current_identity

api=Blueprint('api',__name__)

@api.before_request
@jwt_required()
def before_request():
    current_identity.ping()

@api.app_errorhandler(404)
def page_not_found(e):
    """重新定义了404错误的返回
    """
    return jsonify({'status_code':e.code,'error':e.name,'description':e.description}),404

from . import demo
