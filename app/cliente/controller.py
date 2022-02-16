from app.cliente.models import Cliente
from flask import request
from flask.views import MethodView


class ClienteG(MethodView):
    def post(self):
        body = request.json()

        email = body.get("email")
        senha_hash = body.get("senha_hash")
        nome = body.get("nome")
        cpf = body.get("cpf")
        celular = body.get("celular")
        cep = body.get("cep")
        endereco = body.get("endereco")
        complemento = body.get("complemento")
        idade = body.get("idade")

        