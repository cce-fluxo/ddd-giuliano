from .extensions import db


class BaseModel(db.Model):


    __abstract__ = True


    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Automovel(BaseModel):


    __abstract__ = True


    marca = db.Column(db.String(70))
    modelo = db.Column(db.String(100))
    ano = db.Column(db.String(10))
    preco = db.Column(db.Float)
    motor = db.Column(db.String(50))
    

