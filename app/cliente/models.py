from app.models import BaseModel, db


class Cliente(BaseModel):
    
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    email = db.Column(db.String(70), nullable=False, unique=True)
    senha_hash = db.Column(db.String(70), nullable=False)

    def json(self):
        return{
            "email":self.email
        }