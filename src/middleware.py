from flask_cors import CORS
import os


def setup_cors(app):
    allowed_origin = os.getenv('ALLOWED_ORIGIN') or 'http://localhost:3000'
    CORS(app, resources={r"/*": {"origins": allowed_origin}})
