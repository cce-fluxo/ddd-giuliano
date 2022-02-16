from app.models import BaseModel, db


class Admin(BaseModel):

    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(70), nullable=False, unique=True)
    senha_hash = db.Column(db.String(70), nullable=False)