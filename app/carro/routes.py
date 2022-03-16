from app.carro.controller import CarroG, CarroID
from flask import Blueprint

carro_api = Blueprint('carro_api', __name__)

carro_api.add_url_rule('/carro', view_func=CarroG.as_view('carro_geral'), methods = ['POST', 'GET'])
carro_api.add_url_rule('/carro/<int:id>', view_func=CarroID.as_view('carro_id'), methods = ['GET', 'PATCH', 'DELETE'])
