from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root(name: str = ""):
    if name == "":
        ## /
        return {"message": "Hello world!"}
    else:
        ## /?name=[name]
        return {"message": "Hello " + name + "!"}

@app.get("/url")
async def url():
    return {"url": "http://iesazarquiel.es"}

@app.get("/squarenumber/{number}")
async def squarenumber(number: int = 0):
    return {"square number": number*number}