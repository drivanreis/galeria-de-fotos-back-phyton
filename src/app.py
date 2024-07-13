from flask import Flask
from router import router
from middleware import setup_cors

app = Flask(__name__)

# Configuração do CORS
setup_cors(app)

# Configuração das rotas
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(port=3001)
