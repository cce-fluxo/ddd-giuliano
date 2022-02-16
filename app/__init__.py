from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app():

    app=Flask(__name__)
    app.config.from_object(Config)
    app.debug = True

    db.init_app(app)
    db.migrate.init_app(app, db)

    return app
