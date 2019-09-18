from flask_restful import Api
from flask import Blueprint
from depression_classifier.api.depressionApi import DepressionClfAPI, SuicidalProbaAPI

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(DepressionClfAPI, '/depression_clf')
api.add_resource(SuicidalProbaAPI, '/suicidal_proba')
