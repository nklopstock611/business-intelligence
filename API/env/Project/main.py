from http.client import HTTPException
import os
import numpy as np
import uvicorn
import csv
from io import StringIO
import pandas as pd
from typing import Optional
from django.http import FileResponse
from fastapi import FastAPI, File, UploadFile, Request
from PredictionModel import Model
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from tokenizer_module import tokenizer

app = FastAPI()

# ========= #
# TEMPLATES #
# ========= #

templates = Jinja2Templates(directory="templates")

# ========== #
# CONTROLLER #
# ========== #

@app.get("/")
async def root(request: Request):
   # Devuelve la plantilla index.html
   return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict-text")
async def predict_from_textarea(input: str):
   # Nombre del archivo CSV que se va a escribir
   filename = 'uploaded/review.csv'
   
   # Abrir el archivo CSV en modo escritura
   with open(filename, 'w', newline='') as file:
      # Crear un objeto writer para escribir en el archivo CSV
      writer = csv.writer(file)
      
      # Si el archivo está vacío, escribir la primera fila
      writer.writerow(['', 'review_id'])

      # Esta línea, además de escribir en el csv, genera un id para cada review qu aumenta cada que entra un nuevo registro
      writer.writerow([file.tell()//len(input), input])

   return {"prediction": input}

@app.post("/predict-file")
async def predict_from_file(file: UploadFile = File(...)):
   # Leer el archivo CSV en un DataFrame
   contents = await file.read()
   df = pd.read_csv(StringIO(contents.decode()))

   # Hacer predicciones en los datos CSV usando el modelo de aprendizaje automático
   model = Model()
   predictions = model.make_predictions(df)

   # Unir el CSV de entrada y las predicciones en un único DataFrame
   results_df = pd.concat([df, predictions], axis=1)

   # Guardar el DataFrame de resultados en un archivo CSV en la carpeta "assets"
   filename = os.path.join("assets", f"{file.filename}_results.csv")
   results_df.to_csv(filename, index=False)

   # Devolver el nombre del archivo de resultados como respuesta
   return {"filename": filename}

@app.get("/data/{filename}")
async def get_data(filename: str):
   # Cargar el archivo CSV desde la carpeta "assets"
   filepath = os.path.join("assets", f"{filename}_results.csv")

   # Devolver el archivo como respuesta
   return FileResponse(filepath)
