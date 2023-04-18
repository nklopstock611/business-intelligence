import re
import joblib as jb
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize.casual import casual_tokenize
from nltk.stem.snowball import SnowballStemmer

class Tokenizer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        self.snowball = SnowballStemmer('spanish')

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return [' '.join(self.tokenizer(text)) for text in X]

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)

    # Convertir todas las letras a minúsculas
    def to_lowercase(self, words):
        return [word.lower() for word in words]

    # Reemplazar números en el texto
    def replace_numbers(self, words):
        return [re.sub(r'\d+', '', word) for word in words]

    def preprocessing(self, word):
        words = self.to_lowercase(word)
        words = self.replace_numbers(word)
        return words

    def stemmer(self, words, snowball):
        return [snowball.stem(word) for word in words]

    # Función para tokenizar los reviews
    def tokenizer(self, text):
        text = casual_tokenize(text)
        text = self.stemmer(text, self.snowball)
        text = self.preprocessing(text)
        return text

class Model:

    def __init__(self):
        self.model = None
        self.Tokenizer = Tokenizer()

    def make_predictions(self, data):
        model = jb.load("assets/modelo.joblib")
        result = model.predict(data['review_es'])
        df = pd.DataFrame(result, columns=['sentimiento'])
        return df
        