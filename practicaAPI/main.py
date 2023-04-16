from io import StringIO
import os
from typing import Optional
from django.http import FileResponse
from fastapi import FastAPI, File, UploadFile
from DataModel import DataModel
from joblib import load
import pandas as pd
from PredictionModel import Model
import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import casual_tokenize
import string

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the CSV file into a DataFrame
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode()))
    model = Model()
    # Make predictions on the CSV data using your ML model
    predictions = model.make_predictions(df["review_es"])

    # Join the input CSV and predictions into a single DataFrame
    results_df = pd.concat([df, predictions], axis=1)

    # Save the results DataFrame to a CSV file in the "assets" folder
    filename = os.path.join("assets", f"{file.filename}_results.csv")
    results_df.to_csv(filename, index=False)

    # Return the filename of the results file as a response
    return {"filename": filename}

@app.get("/data/{filename}")
async def get_data(filename: str):
    # Load the CSV file from the "assets" folder
    filepath = os.path.join("assets", f"{filename}_results.csv")

    # Return the file as a response
    return FileResponse(filepath)

def tokenizer(text):
        snowball = SnowballStemmer('spanish')
        words = casual_tokenize(text)
        words = [word.lower() for word in words]
        words = [re.sub(r'\d+', '', word) for word in words]
        words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
        words = [word.encode('ascii', 'ignore').decode('utf-8') for word in words]
        words = [snowball.stem(word) for word in words]
        return words
    