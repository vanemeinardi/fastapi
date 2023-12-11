from fastapi import FastAPI

# Crea una instancia de FastAPI
app = FastAPI()

# Crea un punto de entrada o endpoint
@app.get('/')
def mensaje():
    return 'Hola, bienvenido a FastAPI cambiado de nuevo'

