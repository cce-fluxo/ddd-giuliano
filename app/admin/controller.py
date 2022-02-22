import sqlalchemy
from app.admin.models import Admin
from flask import request, jsonify
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import jwt_required, create_access_token
from app.admin.schemas import AdminSchema, AdminLoginSchema


class AdminG(MethodView):
    def post(self):
        schema = AdminSchema()
        body = request.json

        try:
            admin = schema.load(body)
            admin.save()
            return schema.dump(admin)
        except sqlalchemy.exc.IntegrityError:
            return {"code_status": "esse admin já existe"},400

    def get(self):
        schema = AdminSchema()
        admins = Admin.query.all()
        return jsonify(schema.dump(admins, many=True))


class AdminID(MethodView):
    def get(self, id):
        schema = AdminSchema()
        admin = Admin.query.get_or_404(id)
        return jsonify(schema.dump(admin))


    def patch(self,id):
        body = request.json
        admin = Admin.query.get_or_404(id)
        schema = AdminSchema()

        admin = schema.load(body, instance=admin, partial=True)
        admin.save()
        return schema.dump(admin)
        

    def delete(self, id):
        admin = Admin.query.get_or_404(id)
        admin.delete(admin)
        return {"code_status":"deletado"},200

    
class AdminLogin(MethodView):
    def post(self):
        schema = AdminLoginSchema()
        data = request.json

        email = data["email"]
        senha = data["senha"]

        admin = Admin.query.filter_by(email=email).first()

        if not admin or not bcrypt.checkpw(senha.encode(), admin.senha_hash):
            return {"error":"usuário ou senha inválidos"},400

        token = create_access_token(identity=admin.id)

        return {
            "admin" : schema.dump(admin),
            "token" : token
        }, 200



