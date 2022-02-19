from app.models import Automovel, db


class Carro(Automovel):
    bancos = db.Column(db.String(10))
    