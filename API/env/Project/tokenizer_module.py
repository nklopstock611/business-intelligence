import re
from nltk.tokenize.casual import casual_tokenize
from nltk.stem.snowball import SnowballStemmer

# Convertir todas las letras a minúsculas
def to_lowercase(words):
    return [word.lower() for word in words]

# Reemplazar números en el texto
def replace_numbers(words):
    return [re.sub(r'\d+', '', word) for word in words]

def preprocessing(word):
  words = to_lowercase(word)
  words = replace_numbers(word)
  return words

def stemmer(words, snowball):
  return [snowball.stem(word) for word in words]

# Función para tokenizar los reviews
def tokenizer(text):
  snowball = SnowballStemmer('spanish')
  text = casual_tokenize(text)
  text = stemmer(text, snowball)
  text = preprocessing(text)
  return text