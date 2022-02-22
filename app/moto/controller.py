from app.moto.models import Moto
from flask import request, jsonify
from flask.views import MethodView
from app.moto.schemas import MotoSchema


class MotoG(MethodView):
    def post(self):
        schema = MotoSchema()
        body = request.json

        moto = schema.load(body)
        moto.save()
        return schema.dump(moto)

    def get(self):
        schema = MotoSchema()
        motos = Moto.query.all()
        return jsonify(schema.dump(motos, many=True))


class MotoID(MethodView):
    def get(self, id):
        schema = MotoSchema()
        moto = Moto.query.get_or_404(id)
        return jsonify(schema.dump(moto))


    def patch(self,id):
        body = request.json
        moto = Moto.query.get_or_404(id)
        schema = MotoSchema()

        moot = schema.load(body, instance=moto, partial=True)
        moto.save()
        return schema.dump(moto)
        

    def delete(self, id):
        moto = Moto.query.get_or_404(id)
        moto.delete(moto)
        return {"code_status":"deletado"},200