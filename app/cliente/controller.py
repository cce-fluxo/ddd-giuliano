import sqlalchemy
from app.cliente.models import Cliente
from app.admin.models import Admin
from flask import request, jsonify
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import create_access_token
from app.cliente.schemas import ClienteSchema, LoginSchema
from app.permissions import cliente_jwt_required, admin_jwt_required


class ClientePost(MethodView):
    def post(self):
        schema = ClienteSchema()
        body = request.json

        '''email = body.get("email")
        admin = Admin.query.filter_by(email=email).first()
        if admin:
            return {"code_status":"email já em uso"}, 401'''

        try:
            cliente = schema.load(body)
            cliente.save()
            return schema.dump(cliente),200
        except sqlalchemy.exc.IntegrityError:
            return {"code_status": "esse cliente já existe"},400


class ClienteGet(MethodView):
    def get(self):
        schema = ClienteSchema()
        clientes = Cliente.query.all()
        return jsonify(schema.dump(clientes, many=True)),200


class ClienteID(MethodView):
    decorators = [cliente_jwt_required]
    def get(self, id):
        schema = ClienteSchema()
        cliente = Cliente.query.get_or_404(id)
        return jsonify(schema.dump(cliente)),200


    def patch(self,id):
        body = request.json
        cliente = Cliente.query.get_or_404(id)
        schema = ClienteSchema()

        cliente = schema.load(body, instance=cliente, partial=True)
        cliente.save()
        return schema.dump(cliente),200
        

    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)
        return {"code_status":"deletado"},200


'''class ClienteLogin(MethodView):
    def post(self):
        schema = LoginSchema()
        data = request.json

        email = data["email"]
        senha = data["senha"]

        cliente = Cliente.query.filter_by(email=email).first()

        if not cliente or not bcrypt.checkpw(senha.encode(), cliente.senha_hash):
            return {"error":"usuário ou senha inválidos"},400

        token = create_access_token(identity=cliente.id)

        return {
            "cliente" : schema.dump(cliente),
            "token" : token
        }, 200'''
            