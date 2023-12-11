from fastapi import FastAPI, Body, Path, Query

from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional,List

# crea instancia de fastapi
app = FastAPI()
app.title = 'Aplicacion de ventas'
app.version = '1.0.1'
ventas = [
    {
        "id": 1,
        "fecha": "01/01/23",
        "tienda": "Tienda01",
        "importe": 2500
    },
    {
        "id": 2,
        "fecha": "22/01/23",
        "tienda": "Tienda02",
        "importe": 4500
    }
]
class Ventas(BaseModel):
    id: int = Field(ge=0, le=20, example=3)
    fecha: str = Field(example="01/02/23")
    tienda: str = Field(min_length=4, max_length=10, example="Tienda09")
    importe: float = Field(example=121.0)


@app.get('/', tags=['Inicio'])  # cambio de etiqueta en documentacion
def mensaje():
    return HTMLResponse('<h2>Titulo html desde FastAPI</h2>')


@app.get('/ventas', tags=['Ventas'],response_model = List[Ventas])
def dame_ventas() -> List[Ventas]:
    return JSONResponse(content=ventas)


@app.get('/ventas/{id}', tags=['Ventas'], response_model = Ventas)
def dame_ventas(id: int = Path(ge=1,le=1000)) -> Ventas:
    for elem in ventas:
        if elem['id'] == id:
            return JSONResponse(content=elem)
    return JSONResponse(content=[]) 


@app.get('/ventas/', tags=['Ventas'], response_model=List[Ventas])
# para mas parametros ,id:int
def dame_ventas_por_tienda(tienda: str = Query(min_length=4, max_length=20)) -> List[Ventas]:
    # return tienda
    datos = [elem for elem in ventas if elem['tienda'] == tienda]
    return JSONResponse(content=datos)


@app.post('/ventas', tags=['Ventas'], response_model=dict)
def crea_venta(venta: Ventas) -> dict:
    try:
        ventas.append(venta.dict())
        return JSONResponse(content={'mensaje': 'Venta creada'})
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)



@app.put('/ventas/{id}', tags=['Ventas'], response_model=dict)
def actualiza_ventas(id: int, venta: Ventas) -> dict:
    # recorrer los elementos de la lista
    
    for elem in ventas:        
        if elem['id'] == id:
           elem['fecha'] = venta.fecha
           elem['tienda'] = venta.tienda
           elem['importe'] = venta.importe
    return JSONResponse(content={'mensaje': 'Venta actualizada'})


@app.delete('/ventas/{id}', tags=['Ventas'], response_model=dict)
def borra_venta(id: int) -> dict:
    # recorremos elementos de la lista
    for elem in ventas:
        if elem['id'] == id:
            ventas.remove(elem)
    return JSONResponse(content={'mensaje':'Venta borrada'})