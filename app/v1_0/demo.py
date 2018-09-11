from flask import jsonify
from app.models import User
from . import api

@api.route('/users/<int:id>',methods=['GET'])
def get(id):
    user=User.query.filter_by(id=id).first() 
    returnUser={}
    if user:
        returnUser={
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'member_since': user.member_since
        }
    return jsonify(returnUser),200

