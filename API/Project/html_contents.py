
def html_content_pie_graph():
    return """
    <html>
        <head>
        	<meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            
            <style>
                head {
                    font-family: "Open Sans", sans-serif;
                }
                body {
                    font-family: "Open Sans", sans-serif;
                }
                .btn-custom {
                font-size: 12px;
                border: 1px solid #656565;
                background-color: #EFEFEF;
                border-radius: 2.5px;
                }
                .btn-seleccion {
                    font-size: 12px;
                }
                .btn-custom:hover {
                    background-color: ;
                }
                .btn-custom:focus {
                    outline: none;
                    background-color: #EFEFEF;
                }
            </style>
            
            <center>
                <h1>
                    API de Analisis de Sentimiento
                </h1>
                <h2>
                    Reviews de Peliculas
                </h2>
                <p>
                    En esta API puedes ingresar una review de una pelicula y clasificarla como positiva o negativa.
                </p>
            </center>
        </head>
        <br>
        <body>
            <center>                    
                <h3>Cargar Archivo de Reviews</h2>
                <div>
                    <form method="post" action="/predict-file" enctype="multipart/form-data">
                        <input type="file" name="file" class="btn-seleccion">
                        <button type="submit" class="btn-custom">Clasificar</button>
                    </form>
                </div>
                <div id="plot"></div>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                <script>
                    var data = %s;
                    Plotly.newPlot('plot', data);
                </script>
                <h2>Escribir Review</h2>
                <div>
                    <form method="get" action="/predict-text" id="textarea">
                        <textarea name="input" id="input" rows="4" cols="50" required></textarea>
                        <br><br>
                        <button type="submit" id="submit" class="btn-custom">Clasificar</button>
                    </form>
                </div>
                <div>
                    <a href="/download" download><button class="btn-custom">Descargar archivo</button></a>
                </div>
            </center>
        </body>
    </html>
    """

def html_content_persistent_textarea():
    return """
    <html>
        <head>
        	<meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            
            <style>
                head {
                    font-family: "Open Sans", sans-serif;
                }
                body {
                    font-family: "Open Sans", sans-serif;
                }
                .btn-custom {
                font-size: 12px;
                border: 1px solid #656565;
                background-color: #EFEFEF;
                border-radius: 2.5px;
                }
                .btn-seleccion {
                    font-size: 12px;
                }
                .btn-custom:hover {
                    background-color: ;
                }
                .btn-custom:focus {
                    outline: none;
                    background-color: #EFEFEF;
                }
            </style>
            
            <center>
                <h1>
                    API de Analisis de Sentimiento
                </h1>
                <h2>
                    Reviews de Peliculas
                </h2>
                <p>
                    En esta API puedes ingresar una review de una pelicula y clasificarla como positiva o negativa.
                </p>
            </center>
        </head>
        <br>
        <body>
            <center>                    
                <h3>Cargar Archivo de Reviews</h2>
                <div>
                    <form method="post" action="/predict-file" enctype="multipart/form-data">
                        <input type="file" name="file" class="btn-seleccion">
                        <button type="submit" class="btn-custom">Clasificar</button>
                    </form>
                </div>
                <div id="plot"></div>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                <script>
                    var data = %s;
                    Plotly.newPlot('plot', data);
                </script>
                <h2>Escribir Review</h2>
                <div>
                    <form method="get" action="/predict-text" id="textarea">
                        <textarea name="input" id="input" rows="4" cols="50" required></textarea>
                        <br><br>
                        <button type="submit" id="submit" class="btn-custom">Clasificar</button>
                        <script>
                            var value = document.getElementById('submit').value;
                            localStorage.setItem('submit', value);
                        </scripts>
                    </form>
                </div>
                <div>
                    <a href="/download" download><button class="btn-custom">Descargar archivo</button></a>
                </div>
            </center>
        </body>
    </html>
    """