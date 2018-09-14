# api-jwt

http POST http://127.0.0.1:5000/auth username="admin" password="123"
http http://127.0.0.1:5000/api/v1.0/users/1 Authorization:"JWT <token>"


flask_restplus/api.py
中增加对JWTError的支持，使得返回详细的异常信息



            from flask_jwt import JWTError
            if isinstance(e, HTTPException):
                code = HTTPStatus(e.code)
                if include_message_in_response:
                    default_data = {
                        'message': getattr(e, 'description', code.phrase)
                    }
                headers = e.get_response().headers
            elif isinstance(e,JWTError):
                code = HTTPStatus(e.status_code)
                if include_message_in_response:
                    default_data = {
                        'message': getattr(e, 'description', code.phrase)
                    }
                headers = e.headers

