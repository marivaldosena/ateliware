from flask_restful import Resource, reqparse
from app.models import Repositorio


class RepositorioResource(Resource):

    def get(self, repo_id):
        repo = Repositorio.query.find_by(id=repo_id)

        if repo:
            return {'status': repo.nome}

        return {'status': 'Repositório não encontrado.'}


class RepositorioListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, help='Nome é obrigatório.')

    def get(self):
        return {'status': 'ok'}

    def post(self):
        args = parser.parse_args()
        repo = Repositorio(nome=args['nome'])

        return {'repo': repo.nome}, 201
