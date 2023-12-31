from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Crea una instancia de FastAPI
app = FastAPI()
app.title='Aplicacion de ventas'
app.version='1.0.1'

ventas=[
    {"id":1,
     "fecha":"01/01/23",
     "tienda": "Tienda01",
     "importe": 2500
     },
     {"id":2,
     "fecha":"22/01/23",
     "tienda": "Tienda02",
     "importe": 4500,
     },
    
]

# Crea un punto de entrada o endpoint
@app.get('/', tags=['Inicio']) #cambio de etiqueta en documentacion
def mensaje():
    return HTMLResponse('<h2>Titulo html desde FastAPI <h2>')
@app.get('/ventas', tags=['Ventas'])
def dame_ventas():
    return ventas