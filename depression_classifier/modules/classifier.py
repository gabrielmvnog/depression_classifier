import pickle
import numpy as np


class Classifier():

    def __init__(self):

        with open("depression_classifier/models/svm_tfidf.pickle", "rb") as f:
            self.model = pickle.load(f)

        with open("depression_classifier/models/vectorizer.pickle", "rb") as f:
            self.vectorizer = pickle.load(f)

        self.labels = {
            0: "depression",
            1: "not_depression"
        }

    def predict_sentence(self, sentence: str) -> tuple:
        """
        Uses SVM and TF-IDF to predict the probability of a sentence.

        PARAMETERS
        ----------
            sentece: A string containing a sentece from the user.
        
        RETURNS
        -------
            A tuple (higher probability, label of the max probability)
        """

        sentence = self.vectorizer.transform([sentence]).todense()
        pred = self.model.predict_proba(sentence)[0]

        return max(pred), self.labels[np.argmax(pred)]
