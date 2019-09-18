from flask_restful import Resource
from flask import request
from flasgger import swag_from
from loguru import logger
from depression_classifier.modules.classifier import Classifier
from collections import Counter

clf = Classifier()


class DepressionClfAPI(Resource):

    @swag_from('docs/depre_clf.yml')
    def post(self):

        logger.info('Receiving parameters.')

        req = request.json
        sentence = req['sentence'] if 'sentence' in req.keys() else None

        if sentence:

            porcentage, label = clf.predict_sentence(sentence)

            response_object = {
                "sentence": sentence,
                "result": {
                    "porcentage": porcentage,
                    "label": label
                },
                "message": "CLASSIFICATION_SUCCESS"
            }

            return response_object, 200

        response_object = {
            "message": "PARAMETERS_ERROR"
        }

        return response_object, 500


class SuicidalProbaAPI(Resource):

    def __init__(self):

        self.proba_dict = {
            "not_depression": "no_suicidal_proba",
            "depression": "suicidal_proba"
        }

    @swag_from('docs/suicidal_proba.yml')
    def post(self):

        logger.info('Receiving parameters.')

        req = request.json
        batch = req['batch'] if 'batch' in req.keys() else None

        all_labels = list()

        if batch:

            for sentence in batch:

                _, label = clf.predict_sentence(sentence)
                all_labels.append(label)

            higher_label = Counter(all_labels).most_common(1)[0]
            n_higher_label = higher_label[1]
            total_labels = len(all_labels)

            response_object = {
                "result": {
                    "porcentage": n_higher_label/total_labels,
                    "label": self.proba_dict[higher_label[0]]
                },
                "message": "PROBABILITY_SUCCESS"
            }

            return response_object, 200

        response_object = {
            "message": "PARAMETERS_ERROR"
        }

        return response_object, 500
