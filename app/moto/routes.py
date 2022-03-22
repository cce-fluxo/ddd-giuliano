from app.moto.controller import MotoG, MotoID
from flask import Blueprint


moto_api = Blueprint('moto_api', __name__)

moto_api.add_url_rule('/moto', view_func=MotoG.as_view('moto_geral'), methods = ['POST', 'GET'])
moto_api.add_url_rule('/moto/<int:id>', view_func=MotoID.as_view('moto_id'), methods = ['GET', 'PATCH', 'DELETE'])