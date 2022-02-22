from flask import Blueprint
from app.cliente.controller import ClienteGet, ClientePost, ClienteID, ClienteLogin


cliente_api = Blueprint("cliente_api", __name__)

cliente_api.add_url_rule('/cliente/get/<string:email>', view_func=ClienteGet.as_view('cliente_get'), methods = ['GET'])
cliente_api.add_url_rule('/cliente/post', view_func=ClientePost.as_view('cliente_post'), methods = ['POST'])
cliente_api.add_url_rule('/cliente/<int:id>', view_func=ClienteID.as_view('cliente_id'), methods = ['GET', 'PATCH', 'DELETE'])
cliente_api.add_url_rule('/cliente/login',view_func = ClienteLogin.as_view('cliente_login'), methods = ['POST'])