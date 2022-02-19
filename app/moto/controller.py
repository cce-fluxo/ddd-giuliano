from app.moto.models import Moto
from flask import request
from flask.views import MethodView

class MotoG(MethodView):
    def post(self):
        body = request.json()

        marca = body.get('marca')
        modelo = body.get('modelo')
        ano = body.get('ano')
        cor = body.get('cor')
        preco = body.get('preco')
        motor = body.get('motor')

        if isinstance(marca, str) and isinstance(modelo, str) and isinstance(ano, str) and isinstance(cor, str) and isinstance(preco, float) and isinstance(motor, str):
            
            moto = Moto(marca=marca, modelo=modelo, ano=ano, cor=cor, preco=preco, motor=motor)
            moto.save()
            return moto.json(),200

        return {"code_status":"dados inválidos"},400


    def get(self):
        motos = Moto.query.all()
        body = {}

        for moto in motos:
            body[f"{moto.id}"] = moto.json()
        return body


class MotoID(MethodView):
    def get(self, id):
        moto = Moto.query.get_or_404(id)
        return moto.json()


    def patch(self,id):
        body = request.json()
        moto = Moto.query.get_or_404(id)

        marca = body.get("marca", moto.marca)
        modelo = body.get('modelo', moto.modelo)
        ano = body.get('ano', moto.ano)
        cor = body.get('cor', moto.cor)
        preco = body.get('preco', moto.preco)
        motor = body.get('motor', moto.motor)

        if isinstance(marca, str) and isinstance(modelo, str) and isinstance(ano, str) and isinstance(cor, str) and isinstance(preco, float) and isinstance(motor, str):
            
            moto.marca = marca
            moto.modelo = modelo
            moto.ano = ano
            moto.cor = cor
            moto.preco = preco
            moto.motor = motor

            moto.update()
            return moto.json(),200

        return {"code_status":"dados inválidos"},400


    def delete(self, id):
        moto = Moto.query.get_or_404(id)
        moto.delete()
        return {"code_status":"moto deletada"},200
    