from app.extensions import ma
from app.cliente.models import Cliente


class ClienteSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Cliente
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    email = ma.Email(required=True)
    senha = ma.String(load_only=True)
    nome = ma.String()
    cpf = ma.String()
    culular = ma.String()
    cep = ma.String()
    endereco = ma.String()
    complemento = ma.String()
    idade = ma.Integer()
