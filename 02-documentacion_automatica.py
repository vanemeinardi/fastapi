from fastapi import FastAPI

# Crea una instancia de FastAPI
app = FastAPI()
app.title='Aplicacion de ventas'
app.version='1.0.1'

# Crea un punto de entrada o endpoint
@app.get('/', tags=['Inicio']) #cambio de etiqueta en documentacion
def mensaje():
    return 'Hola, bienvenido a FastAPI cambiado de nuevo'