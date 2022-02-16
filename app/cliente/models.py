from app.models import BaseModel, db


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