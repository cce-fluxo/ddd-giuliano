from flask import Blueprint
from app.cliente.controller import ClienteG, ClienteID, ClienteLogin


cliente_api = Blueprint("cliente_api", __name__)

cliente_api.add_url_rule('/cliente', view_func=ClienteG.as_view('cliente_geral'), methods = ['POST', 'GET'])
cliente_api.add_url_rule('/cliente/<int:id>', view_func=ClienteID.as_view('cliente_id'), methods = ['GET', 'PATCH', 'DELETE'])
cliente_api.add_url_rule('/cliente/logjn', view_func=ClienteID.as_view('cliente_id'), methods = ['POST'])