import string
import re

import numpy as np
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.casual import casual_tokenize
from nltk.stem.snowball import SnowballStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import FunctionTransformer

from sklearn.metrics import ConfusionMatrixDisplay, precision_score, recall_score, f1_score
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from joblib import dump, load
from sklearn.base import BaseEstimator, TransformerMixin

# class Tokenizer(BaseEstimator, TransformerMixin):
    
#     def __init__(self):
#         self.snowball = SnowballStemmer('spanish')

#     def fit(self, X, y=None):
#         return self
    
#     def transform(self, X):
#         return [' '.join(self.tokenizer(text)) for text in X]

#     def fit_transform(self, X, y=None):
#         self.fit(X, y)
#         return self.transform(X)

#     # Convertir todas las letras a minúsculas
#     def to_lowercase(self, words):
#         return [word.lower() for word in words]

#     # Reemplazar números en el texto
#     def replace_numbers(self, words):
#         return [re.sub(r'\d+', '', word) for word in words]

#     def preprocessing(self, word):
#         words = self.to_lowercase(word)
#         words = self.replace_numbers(word)
#         return words

#     def stemmer(self, words, snowball):
#         return [snowball.stem(word) for word in words]

#     # Función para tokenizar los reviews
#     def tokenizer(self, text):
#         text = casual_tokenize(text)
#         text = self.stemmer(text, self.snowball)
#         text = self.preprocessing(text)
#         return text
