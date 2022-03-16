from app.moto.models import Moto
from app.extensions import ma


class MotoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Moto
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    marca = ma.String()
    modelo = ma.String()
    ano = ma.String()
    cor = ma.String()
    preco = ma.String()
    motor = ma.String()
