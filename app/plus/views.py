from . import plus
from ..models import User
from flask_restplus import Api, Resource, fields
from flask_jwt import jwt_required, current_identity


@plus.before_request
def before_request():
    pass

api = Api(plus)

parser = api.parser()
parser.add_argument('Authorization', help='令牌:JWT <token>', location='headers')

@api.route("/hello")
@api.expect(parser)
class HelloWorld(Resource):
    @jwt_required()
    def get(self):
        current_identity.ping()
        return {'hello': 'world'},200


ns = api.namespace('users', description='用户接口')

model_user = ns.model('User', {
    'username': fields.String,
    'uri': fields.Url('plus.user',absolute=True)
})

@ns.route('/<int:id>',endpoint='user')
@ns.expect(parser)
class UserApi(Resource):

    @jwt_required()
    @ns.doc(params={'id':'用户编码'})
    #@ns.marshal_with(model_user,mask='',code=200)
    def get(self, id):
        user=User.query.filter(User.id==id).first()
        return {'user':user.id,
                'username':user.username,
                'email':user.email},200
