# API que expone un modelo de Análisis y Clasificación de Sentimiento de Reviews de Películas.

Antes de ejecutar la API, se deben instalar las librerías usadas. Esto se puede hacer corriendo la siguiente línea en una consola:
```bash
pip install -r requirements.txt
```
(esto se puede demorar)

Luego, hay que revisar rutas. Si en la primera corrida no funciona, en los archivos "main.py" y "PredictionModel.py" cambien la siguiente línea:
```bash
parent = os.path.dirname(os.path.dirname(os.path.dirname(current)))
```
por:
```bash
parent = os.path.dirname(os.path.dirname(current))
```

Ya con todo instalado, hay que meterse a la carpeta del proyecto:
```bash
cd API/Project
```

Ya, por último, falta correr la API:
```bash
uvicorn main:app --reload
```
