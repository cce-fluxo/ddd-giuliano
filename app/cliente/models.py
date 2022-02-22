from app.models import BaseModel, db
import bcrypt


class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(70), nullable=False, unique=True)
    senha_hash = db.Column(db.String(70), nullable=False)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(15), nullable=False, unique=True)
    celular = db.Column(db.String(20), nullable=False, unique=True)
    cep = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(30))
    idade = db.Column(db.SmallInteger)
    role = 'cliente'

    def json(self):
        return{
            "email":self.email,
            "nome":self.nome,
            "cpf":self.cpf,
            "celular":self.celular,
            "cep":self.cep,
            "endereco":self.endereco,
            "complemento":self.complemento,
            "idade":self.idade
        }

    @property
    def senha(self):
        raise AttributeError('senha is not a readable attribute')
    
    @senha.setter
    def senha(self, senha):
        self.senha_hash = bcrypt.hashpw(
            senha.encode(), bcrypt.gensalt())