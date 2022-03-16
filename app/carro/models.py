from markupsafe import _MarkupEscapeHelper
from app.models import Automovel, db


class Carro(Automovel):

    __tablename__ = "carro"

    bancos = db.Column(db.SmallInteger)

    def json(self):
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "ano" : self.ano,
            "cor" : self.cor,
            "preco" : self.preco,
            "motor" : self.motor,
            "bancos" : self.bancos
        }