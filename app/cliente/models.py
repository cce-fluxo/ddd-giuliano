from app.models import BaseModel, db
import bcrypt
from app.storage.models import storage
from flask_jwt_extended import create_access_token


class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(70), nullable=False, unique=True)
    senha_hash = db.Column(db.String(), nullable=False)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(15), nullable=False, unique=True)
    celular = db.Column(db.String(20), nullable=False, unique=True)
    cep = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(30))
    data_de_nascimento = db.Column(db.String(30))
    '''avatar = db.Column(db.String(64), unique = True, default = None)'''
    role = 'cliente'


    @property
    def senha(self):
        raise AttributeError('senha is not a readable attribute')
    
    @senha.setter
    def senha(self, senha):
        self.senha_hash = senha.encode

    '''@property
    def avatar_url(self):
        if self.avatar:
            return storage.get_url(self.avatar)
        return None

    @avatar_url.setter
    def avatar_url(self,name):
        if self.avatar:
            storage.delete_object(self.avatar)
        self.avatar = name'''