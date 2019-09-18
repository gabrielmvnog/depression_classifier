from flasgger import Swagger
from flask import Flask, jsonify
from loguru import logger

from depression_classifier.api import api_bp

__version__ = '0.0.1'

template = {
    "swagger": "2.0",
    "info": {
        "title": "Classificador de depressão",
        "description": "Classificação de depressão.",
        "version": __version__
    },
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

app = Flask(__name__)
Swagger(app=app, template=template)

app.register_blueprint(api_bp, url_prefix='/api')
logger.start('depre_clf.log', level='INFO', format="{time} {level} {message}",
             backtrace=False, rotation='25 MB')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'status': 404, 'mensagem': 'URL não encontrada.'}), 404


@app.errorhandler(500)
def server_errror(e):
    return jsonify({'status': 500, 'mensagem': 'Erro interno.'}), 500
