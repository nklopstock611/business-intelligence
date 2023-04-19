import re
import sys
import os
import pandas as pd
import joblib as jb

from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize.casual import casual_tokenize
from nltk.stem.snowball import SnowballStemmer

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(os.path.dirname(os.path.dirname(current)))

sys.path.append(parent)

# from Notebook import tokenizer


class Model:

    def __init__(self):
        self.model = None

    def make_predictions(self, data):
        model = jb.load("assets/modelo.joblib")
        result = model.predict(data['review_es'])
        df = pd.DataFrame(result, columns=['sentimiento'])
        return df
        