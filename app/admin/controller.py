from app.admin.models import Admin
from flask import request
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import jwt_required, create_access_token


class AdminG(MethodView):
    def post(self):
        body = request.json()

        email = body.get("email")
        senha = body.get("senha")

        if isinstance(email,str) and isinstance(senha,str):

            admin = admin.query.filter_by(email=email)
            if admin:
                return {"code_status":"esse admin já extiste"},400
            
            senha_hash = bcrypt.hashpw(senha.encode, bcrypt.gensalt())
            admin = Admin(email=email, senha_hash=senha_hash)
            admin.save()

            return admin.json()

        return {"code_status":"dados inválidos"},400


    def get(self):
        admins = Admin.query.all()
        body = {}
        for admin in admins:
            body[f"{admin.id}"] = admin.json()
        return body


class AdminID(MethodView):
    def get(self, id):
        admin = Admin.get_or_404(id)
        return admin.json()


    def patch(self, id):
        body = request.json()
        admin = Admin.query.get_or_404(id)

        email = body.get("email", admin.email)
        senha = body.get("senha", admin.senha)

        if isinstance(email, str) and isinstance(senha, str):

            senha_hash = bcrypt.hashpw(senha.encode, bcrypt.gensalt())

            admin.email = email
            admin.senha_hash = senha_hash

            admin.update()
            return admin.json(),200

        return {"code_status" : "dados inválidos"},400

    
    def delete(self, id):
        admin = Admin.query.get_or_404(id)
        admin.delete()
        return {"code_status" : "admin deletado"},200

    
class AdminLogin(MethodView):
    def post(self):
        body = request.json()
        email = body.get("email")
        senha = body.get("senha")

        senha_hash = bcrypt.hashpw(senha.encode, bcrypt.gensalt())

        admin = Admin.query.filter_by(id=id).first()

        if not admin or not senha_hash:
            return {"code_status" : "usuário ou senha inválidos"}
        token = create_access_token(identity = admin.id)

        return {'token':token},200



