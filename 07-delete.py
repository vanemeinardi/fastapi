from fastapi import FastAPI, Body
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
@app.get('/ventas/{id}', tags=['Ventas'])
def dame_ventas(id:int):
    for elem in ventas:
        if elem['id']==id:
            return elem
    return []
@app.get('/ventas/', tags=['Ventas'])
def dame_ventas_por_tienda(tienda:str):
    #return tienda
    return [elem for elem in ventas if elem['tienda']==tienda] 
@app.post('/ventas', tags=['Ventas'])
def crea_venta(id: int = Body(), fecha: str = Body(), tienda: str = Body(), importe: float = Body()):
    #return tienda
    ventas.append(
        {
            "id": id,
            "fecha": fecha,
            "tienda": tienda,
            "importe": importe
        }
    )
    return ventas
@app.put('/ventas/{id}',tags=['Ventas'])
def actualiza_ventas(id: int, fecha: str = Body(), tienda: str = Body(), importe: float = Body()):
    # recorrer los elementos de la lista
    for elem in ventas:
        if elem['id'] == id:
           elem['fecha'] = fecha
           elem['tienda'] = tienda
           elem['importe'] = importe
    return ventas
@app.delete('/ventas/{id}',tags=['Ventas'])
def borra_venta(id:int):
    # recorremos elementos de la lista
    for elem in ventas:
        if elem['id'] == id:
            ventas.remove(elem)
    return ventas