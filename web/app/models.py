from .extensions import db


class Repositorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    github_id = db.Column(db.Integer)
    nome = db.Column(db.String)
    url = db.Column(db.String)
