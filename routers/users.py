from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

lista_usuarios = [
    {"id": 1, "username": "manolo", "email": "manolo@iesazarquiel.es"},
    {"id": 2, "username": "alicia", "email": "alicia@iesazarquiel.es"},
    {"id": 3, "username": "paco", "email": "paco@iesazarquiel.es"},
    {"id": 4, "username": "lucia", "email": "lucia@iesazarquiel.es"}
]

@router.get("/users")
async def users():
    return lista_usuarios