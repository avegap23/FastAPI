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

@router.post("/user")
async def newUser(user: User):
    if any(user.id == user_stored.id for user_stored in users_fake_db):
        return {"error": "id ya usado"}
    
    users_fake_db.append(user)
    return user