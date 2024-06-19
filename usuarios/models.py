from db import db
from passlib.hash import pbkdf2_sha256

class Users(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = pbkdf2_sha256.hash(senha)

    def save(self):
        db.session.add(self)
        db.session.commit()
