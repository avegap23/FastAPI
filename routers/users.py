from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

user_list = [
    {"id": 1, "username": "manolo", "email": "manolo@iesazarquiel.es"},
    {"id": 2, "username": "alicia", "email": "alicia@iesazarquiel.es"},
    {"id": 3, "username": "paco", "email": "paco@iesazarquiel.es"},
    {"id": 4, "username": "lucia", "email": "lucia@iesazarquiel.es"}
]

class User(BaseModel):
    id: int
    username: str
    email: str

users_fake_db = [
    User(id=1, username="manolo", email="manolo@iesazarquiel.es"),
    User(id=2, username="alicia", email="alicia@iesazarquiel.es"),
    User(id=3, username="paco", email="paco@iesazarquiel.es"),
    User(id=4, username="lucia", email="lucia@iesazarquiel.es")
]

@router.get("/usersjson")
async def usersjson():
    return user_list

@router.get("/users")
async def users():
    return users_fake_db

@router.get("/user/{id}")
async def userById(id: int):
    return search_user_by_id(id)

@router.post("/user")
async def newUser(user: User):
    if any(user.id == user_stored.id for user_stored in users_fake_db):
        return {"error": "id ya usado"}
    
    users_fake_db.append(user)
    return user

@router.delete("/user/{id}")
async def deleteUser(id: int):
    found_user = search_user_by_id(id)
    if type(found_user) == User:
        users_fake_db.remove(found_user)
        return {"mensaje": "usuario eliminado correctamente"}
    return {"error": "no se puede eliminar el usuario"}

@router.put("/user")
async def update(user: User):
    found_user = search_user_by_id(user.id)
    if type(found_user) == User:
        found_user.username = user.username
        found_user.email = user.email
        return {"mensaje": "usuario actualizado correctamente"}
    return {"error": "no se puede actualizar el usuario"}

def search_user_by_id(id: int):
    for user in users_fake_db:
        if user.id == id:
            return user
    return {"error": "no se encuentra el usuario"}