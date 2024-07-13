from flask import Blueprint
from routes.index import index_route
from routes.photos import photos_route
from routes.upload import upload_route

router = Blueprint('router', __name__)

# Registrar rotas
router.add_url_rule('/', view_func=index_route, methods=['GET'])
router.add_url_rule('/photos', view_func=photos_route, methods=['GET'])
router.add_url_rule('/upload', view_func=upload_route, methods=['POST'])
