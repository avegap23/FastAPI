from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root(nombre: str = ""):
    if nombre == "":
        return {"mensaje": "Hola " + nombre}
    else:
        return {"mensaje": "Hola mundo"}

@app.get("/url")
async def url():
    return {"url": "http://iesazarquiel.es"}

@app.get("/cuadrado/{numero}")
async def cuadrado(numero: int = 0):
    return {"cuadrado": numero*numero}