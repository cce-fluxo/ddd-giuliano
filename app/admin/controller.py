from app.admin.models import Admin
from flask import request
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import jwt_required, create_access_token


class UserG(MethodView):
    def post():
        body = request.json()

        email = body.get("email")
        senha = body.get("senha")

        if isinstance(email,str) and isinstance(senha,str):

            admin = admin.query.filter_by(email=email)
            if admin:
                return {"code_status":"esse admin já extiste"},400
            
            senha_hash = bcrypt.hashpw(senha.encode, bcrypt.gensalt())
            admin = Admin(email=email, senha=senha)
            admin.save()

            return admin.json()

        return {"code_status":"dados inválidos"}


    def get():
        pass


