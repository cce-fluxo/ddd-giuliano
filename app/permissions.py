from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.cliente.models import Cliente


def cliente_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('id'):
            if kwargs.get('id') != get_jwt_identity():
                return {'msg': 'Unauthorized user',
                        'id': kwargs.get('id'),
                        'jwt': get_jwt_identity()}, 401
            else:
                check = Cliente.query.get_or_404(get_jwt_identity())
                if check.role == 'cliente':
                    return func(*args, **kwargs)
                else:
                    return {'msg': 'Somente clientes only'}, 401
        if kwargs.get('id'):
            cliente = Cliente.query.get_or_404(kwargs.get('id'))
            if cliente.id != get_jwt_identity():
                return {'msg': 'Cliente não autorizado'}, 401
            else:
                return func(*args, **kwargs)
    return wrapper