from app.models import BaseModel, db
import bcrypt


class Admin(BaseModel):

    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(70), nullable=False, unique=True)
    senha_hash = db.Column(db.String(), nullable=False)
    role = 'admin'

    def json(self):
        return {
            "email": self.email
        }


    @property
    def senha(self):
        raise AttributeError('senha is not a readable attribute')
    
    @senha.setter
    def senha(self, senha):
        self.senha_hash = bcrypt.hashpw(
            senha.encode(), bcrypt.gensalt())