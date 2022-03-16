from markupsafe import _MarkupEscapeHelper
from app.models import Automovel


class Moto(Automovel):

    __tablename__ = 'moto'

    def json(self):
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "ano" : self.ano,
            "cor" : self.cor,
            "preco" : self.preco,
            "motor" : self.motor
        }