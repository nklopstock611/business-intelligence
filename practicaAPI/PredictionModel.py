from joblib import load
import joblib
import pandas as pd
import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import casual_tokenize
import string

class Model:

    def __init__(self):
        self.model = joblib.load("assets/model2.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        df = pd.DataFrame(result, columns=['prediction'])
        return df
    
    def to_lowercase(words):
        return [word.lower() for word in words]

    def replace_numbers(words):
        return [re.sub(r'\d+', '', word) for word in words]

    def remove_punctuation(words):
        return [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    def remove_non_ascii(words):
        return [word.encode('ascii', 'ignore').decode('utf-8') for word in words]

    def tokenizer(text):
        snowball = SnowballStemmer('spanish')
        words = casual_tokenize(text)
        words = [word.lower() for word in words]
        words = [re.sub(r'\d+', '', word) for word in words]
        words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
        words = [word.encode('ascii', 'ignore').decode('utf-8') for word in words]
        words = [snowball.stem(word) for word in words]
        return words
    