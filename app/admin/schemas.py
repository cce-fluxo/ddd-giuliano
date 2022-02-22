from app.extensions import ma
from app.admin.models import Admin


class AdminSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Admin
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    email = ma.Email(required=True)
    senha = ma.String(load_only=True)


class AdminLoginSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Admin
        load_instance = True
        ordered = True

    email = ma.Email(required=True)
    senha = ma.String(required=True, load_only=True)