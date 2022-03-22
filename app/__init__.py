from flask import Flask
from .extensions import db, migrate, jwt, ma
from .config import Config
from app.cliente.routes import cliente_api
from app.admin.routes import admin_api
from app.carro.routes import carro_api
from app.moto.routes import moto_api
from app.storage.routes import storage_api
from app.esquecisenha.routes import esquecisenha_api
from app.extensions import mail as mail

def create_app():

    app=Flask(__name__)
    app.config.from_object(Config)
    app.debug=True

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    app.register_blueprint(cliente_api)
    app.register_blueprint(admin_api)
    app.register_blueprint(carro_api)
    app.register_blueprint(moto_api)
    app.register_blueprint(storage_api)
    app.register_blueprint(esquecisenha_api)

    return app
