from fastapi import APIRouter, HTTPException, status
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

@router.get("/users/json")
async def usersjson():
    return user_list

@router.get("/users", response_model=list[User])
async def users():
    return users_fake_db

@router.get("/user/{id}")
async def userById(id: int):
    return search_user_by_id(id)

@router.post("/user/new", status_code=status.HTTP_201_CREATED, response_model=User)
async def newUser(user: User):
    if any(user.id == user_stored.id for user_stored in users_fake_db):
        # return {"error": "id already taken"}
        raise HTTPException(status.HTTP_409_CONFLICT, detail="id already")
    users_fake_db.append(user)
    return user

@router.delete("/user/delete/{id}")
async def deleteUser(id: int):
    found_user = search_user_by_id(id)
    if type(found_user) == User:
        users_fake_db.remove(found_user)
        return {"message": "user successfuly deleted"}
    # return {"error": "can't delete user"}
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="can't delete user")

@router.put("/user/edit")
async def update(user: User):
    found_user = search_user_by_id(user.id)
    if type(found_user) == User:
        found_user.username = user.username
        found_user.email = user.email
        return {"message": "user succesfuly updated"}
    # return {"error": "can't update user"}
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")

def search_user_by_id(id: int):
    for user in users_fake_db:
        if user.id == id:
            return user
    # return {"error": "user not found"}
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")