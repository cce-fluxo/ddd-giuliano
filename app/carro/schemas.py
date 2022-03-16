from app.carro.models import Carro
from app.extensions import ma


class CarroSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Carro
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    marca = ma.String()
    modelo = ma.String()
    ano = ma.String()
    cor = ma.String()
    preco = ma.String()
    motor = ma.String()
    banco = ma.String()
