from app.carro.models import Carro
from flask import request, jsonify
from flask.views import MethodView
from app.carro.schemas import CarroSchema


class CarroG(MethodView):
    def post(self):
        schema = CarroSchema()
        body = request.json

        carro = schema.load(body)
        carro.save()
        return schema.dump(carro)

    def get(self):
        schema = CarroSchema()
        carros = Carro.query.all()
        return jsonify(schema.dump(carros, many=True))


class CarroID(MethodView):
    def get(self, id):
        schema = CarroSchema()
        carro = Carro.query.get_or_404(id)
        return jsonify(schema.dump(carro))


    def patch(self,id):
        body = request.json
        carro = Carro.query.get_or_404(id)
        schema = CarroSchema()

        carro = schema.load(body, instance=carro, partial=True)
        carro.save()
        return schema.dump(carro)
        

    def delete(self, id):
        carro = Carro.query.get_or_404(id)
        carro.delete(carro)
        return {"code_status":"deletado"},200