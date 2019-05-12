from flask_restful import Resource
from app.models import Repositorio

class RepositorioResource(Resource):
    def get(self):
        repo = Repositorio(nome='Teste')
        return {'status': repo.nome}
