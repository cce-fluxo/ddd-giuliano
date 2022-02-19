from app.carro.models import Carro
from flask import request
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import jwt_required, create_access_token


class CarroG(MethodView):
    def post(self):
        body = request.json()

        marca = body.get('marca')
        modelo = body.get('modelo')
        ano = body.get('ano')
        preco = body.get('preco')
        motor = body.get('motor')
        bancos = body.get('bancos')

        if isinstance(marca, str) and isinstance(modelo, str) and isinstance(ano, str) and isinstance(preco,float) and isinstance(motor, str) and isinstance(bancos, int):
            carro = Carro(marca=marca, modelo=modelo, ano=ano, preco=preco, motor=motor, bancos=bancos)
            carro.save()

            return carro.json()

        return {"code_status":"dados inválidos"},400

    
    def get(self):

        carros = Carro.query.all()
        body = {}
        
        for carro in carros:
            body[f"{carro.id}"] = carro.json()
        return body


class CarroID:
    def get(self, id):
        carro = Carro.query.get_or_404(id)
        return carro.json()

    def patch(self, id):
        body = request.json()
        carro = Carro.get_or_404(id)

        marca = body.get("marca", carro.marca)
        modelo = body.get("modelo", carro.modelo)
        ano = body.get("ano", carro.ano)
        preco = body.get("preco", carro.preco)
        motor = body.get("motor", carro.motor)
        bancos = body.get("bancos", carro.bancos)

        if isinstance(marca, str) and isinstance(modelo, str) and isinstance(ano,str) and isinstance(preco, float) and isinstance(motor, str) and isinstance(bancos, int):
            carro.marca = marca
            carro.modelo = modelo
            carro.ano = ano
            carro.preco = preco
            carro.motor = motor
            carro.bancos = bancos

            carro.update()
            return carro.json(),200
        
        return {"code_status" : "dados inválidos"},400

    def delete(self, id):
        carro = Carro.query.get_or_404(id)
        carro.delete()
        return {"carro deletado"}, 200