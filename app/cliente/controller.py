import sqlalchemy
from app.cliente.models import Cliente
from flask import request, jsonify
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from app.cliente.schemas import ClienteSchema, LoginSchema


class ClienteG(MethodView):
    def post(self):
        schema = ClienteSchema()
        body = request.json

        try:
            cliente = schema.load(body)
            cliente.save()
            return schema.dump(cliente)
        except sqlalchemy.exc.IntegrityError:
            return {"code_status": "esse cliente já existe"},400


    def get(self):
        schema = ClienteSchema()
        clientes = Cliente.query.all()
        return jsonify(schema.dump(clientes, many=True))


class ClienteID(MethodView):
    def get(self, id):
        schema = ClienteSchema()
        cliente = Cliente.query.get_or_404(id)
        return jsonify(schema.dump(cliente))


    def patch(self,id):
        body = request.json
        cliente = Cliente.query.get_or_404(id)
        schema = ClienteSchema()

        cliente = schema.load(body, instance=cliente, partial=True)
        cliente.save()
        return schema.dump(cliente)
        
        '''email = body.get("email", cliente.email)

        senha_hash = cliente.senha_hash
        if "senha" in body:
            if isinstance(body.get("senha"), str):
                senha = body.get("senha")
                senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        nome = body.get("nome", cliente.nome)
        cpf = body.get("cpf", cliente.cpf)
        celular = body.get("celular", cliente.celular)
        cep = body.get("cep", cliente.cep)
        endereco = body.get("endereco", cliente.endereco)
        complemento = body.get("complemento", cliente.complemento)
        idade = body.get("idade", cliente.idade)

        if isinstance(email, str) and isinstance(nome, str) and isinstance(cpf, str) and isinstance(celular, str) and isinstance(cep, str) and isinstance(endereco, str) and isinstance(complemento, str) and isinstance(idade, int):
            cliente.email = email
            cliente.senha_hash = senha_hash
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.celular = celular
            cliente.cep = cep
            cliente.endereco = endereco
            cliente.complemento = complemento
            cliente.idade = idade

            cliente.update()
            return cliente.json(),200
        return {"code_status":"dados inválidos"},400'''


    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)
        return {"code_status":"deletado"},200


'''class ClienteLogin(MethodView):
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        cliente = Cliente.query.filter_by(email=email).first()

        if not cliente or not bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) == cliente.senha_hash:
            return {'code_status':'usuário ou senha inválidos'},400

        token = create_access_token(identity=cliente.id)

        return {'token':token},200'''

class ClienteLogin(MethodView):
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
        }, 200
            
