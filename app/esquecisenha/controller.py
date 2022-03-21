from flask import request,render_template, jsonify, abort, make_response
from flask.views import MethodView
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended.utils import decode_token
from flask_mail import Message
from app.extensions import mail, db
from app.esquecisenha.schemas import EmailSchema,SenhaSchema
from app.cliente.models import Cliente
from sqlalchemy import exc


class SenhaMail(MethodView):#/send_mail/reset
    def post(self):
        schema = EmailSchema()
        dados = schema.load(request.json)
        cliente = Cliente.query.filter_by(email=dados['email']).first()
        if cliente:
            token = create_access_token(identity=cliente.id,additional_claims={'user_type' : "cliente"})
            refresh_token = create_refresh_token(identity=cliente.id, additional_claims={'user_type': "cliente"})
    
        else:
            return {"Error":"Esse email não está cadastrado"}, 400
        msg = Message(sender = 'giuliano.domiciano@poli.ufrj.br',
        recipients=[cliente.email],
        subject = 'Mudança de senha',
        html = render_template('recupera.html', nome = cliente.nome, link=token))
        mail.send(msg)
        return {"Resultado":"envio feito"},200

class SenhaNova(MethodView): #/reset/<token>
    def patch(self,token):
        schema = SenhaSchema()
        dados = schema.load(request.json)

        token = decode_token(token)
        
        if token['user_type']=="cliente":
            cliente = Cliente.query.filter_by(id = token["sub"]).first()
        
        if not cliente: return {"Error":"Token Inválido ou expirado"},404
        cliente.senha = dados["senha"]
        db.session.add(cliente)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        msg = Message(sender = 'giuliano.domiciano@poli.ufrj.br',
        recipients=[cliente.email],
        subject = 'Senha Alterada',
        html = render_template('altera.html', nome = cliente.nome))
        mail.send(msg)
        mail.send(msg)
        return {},200