from datetime import datetime
from . import db

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    dentro_dieta = db.Column(db.Boolean, default=True)
