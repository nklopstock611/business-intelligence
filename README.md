# API que expone un modelo de Análisis y Clasificación de Sentimiento de Reviews de Películas.

Antes de ejecutar la API, se deben instalar las librerías usadas. Esto se puede hacer corriendo la siguiente línea en una consola (esto se puede demorar):
```bash
$ pip install -r requirements.txt
```
<br><br>
Luego, hay que revisar rutas. Si en la primera corrida no funciona, en los archivos "main.py" y "PredictionModel.py" cambien la siguiente línea:
```bash
parent = os.path.dirname(os.path.dirname(os.path.dirname(current)))
```
por:
```bash
parent = os.path.dirname(os.path.dirname(current))
```
<br><br>
Ya con todo instalado, hay que meterse a la carpeta del proyecto:
```bash
$ cd API/Project
```
<br><br>
Ya, por último, falta correr la API:
```bash
$ uvicorn main:app --reload
```
<br><br>
Una vez la API esté corriendo, van a aparecer dos opciones de predicción. La primera es cargar un archivo. Importante aclarar que el archivo debe ser .csv, tener contexto de reviews de películas en español y seguir el siguiente formato:
```bash
+-----+-----------+
| id  | review_es |
+-----+-----------+
| int |  string   |
+-----+-----------+
```
La otra opción es escribir una reseña ahí mismo. Por favor, no usar tíldes en el input.
