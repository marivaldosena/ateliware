from app.extensions import api
from .repositorios_routes import RepositorioResource

api.add_resource(RepositorioResource, '/')
