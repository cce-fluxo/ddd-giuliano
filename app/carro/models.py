from markupsafe import _MarkupEscapeHelper
from app.models import Automovel, db


class Carro(Automovel):

    __tablename__ = "carro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    bancos = db.Column(db.String(10))

    def json(self):
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "ano" : self.ano,
            "preco" : self.preco,
            "motor" : self.motor,
            "bancos" : self.bancos
        }