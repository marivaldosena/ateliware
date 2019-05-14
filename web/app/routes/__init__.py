from app.extensions import api
from .repositorios_routes import (
    RepositorioResource,
    RepositorioListResource
)

api.add_resource(RepositorioListResource, '/')
api.add_resource(RepositorioResource, '/<string:repo_id>')
