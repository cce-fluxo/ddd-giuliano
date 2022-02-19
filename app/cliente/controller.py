from app.cliente.models import Cliente
from flask import request
from flask.views import MethodView
import bcrypt


class ClienteG(MethodView):
    def post(self):
        body = request.json()

        email = body.get("email")
        senha = body.get("senha")
        nome = body.get("nome")
        cpf = body.get("cpf")
        celular = body.get("celular")
        cep = body.get("cep")
        endereco = body.get("endereco")
        complemento = body.get("complemento")
        idade = body.get("idade")

        if isinstance(email, str) and isinstance(senha, str) and isinstance(nome, str) and isinstance(cpf, str) and isinstance(celular, str) and isinstance(cep, str) and isinstance(endereco, str) and isinstance(complemento, str) and isinstance(idade, int):
            cliente = Cliente.query.filter_by(email=email).first() and Cliente.query.filter_by(cpf=cpf).first() and Cliente.query.filter_by(celular=celular).first()
            if cliente:
                return{"code_status": "esse cliente já existe"},400

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            cliente = Cliente(email=email, senha=senha, nome=nome, cpf=cpf, celular=celular, cep=cep, endereco=endereco, complemento=complemento, idade=idade)
            cliente.save()

            return cliente.json()
        return {"code_status": "dados inválidos"},400


    def get(self):
        clientes = Cliente.query.all()
        body = {}
        for cliente in clientes:
            body[f"{cliente.id}"] = cliente.json()
        return body


class ClienteID(MethodView):
    def get(self, id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json()


    def patch(self,id):
        body = request.json()
        cliente = Cliente.query.get_or_404(id)

        
        email = body.get("email", cliente.email)
        senha = body.get("senha", cliente.senha)
        nome = body.get("nome", cliente.nome)
        cpf = body.get("cpf", cliente.cpf)
        celular = body.get("celular", cliente.celular)
        cep = body.get("cep", cliente.cep)
        endereco = body.get("endereco", cliente.endereco)
        complemento = body.get("complemento", cliente.complemento)
        idade = body.get("idade", cliente.idade)

        if isinstance(email, str) and isinstance(senha, str) and isinstance(nome, str) and isinstance(cpf, str) and isinstance(celular, str) and isinstance(cep, str) and isinstance(endereco, str) and isinstance(complemento, str) and isinstance(idade, int):
            senha_hash = bcrypt.hashpw(senha.enconde(), bcrypt.gensalt())
            cliente.email = email
            cliente.senha = senha
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.celular = celular
            cliente.cep = cep
            cliente.endereco = endereco
            cliente.complemento = complemento
            cliente.idade = idade

            cliente.update()
            return cliente.json(),200
        return {"code_status":"dados inválidos"},400


def delete(self, id):
    cliente = Cliente.query.get_or_404
    cliente.delete(cliente)
    return {"code_status":"deletado"},200

