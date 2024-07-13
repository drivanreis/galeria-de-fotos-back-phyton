import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

allowed_origin = os.getenv('ALLOWED_ORIGIN', 'http://localhost:3000')


app = Flask(__name__)


@app.route('/')
def index_route():
    return jsonify(
        message=f'Backend Rodando! E a origem permitida e: {allowed_origin}'
        )


if __name__ == '__main__':
    app.run(port=3001)
