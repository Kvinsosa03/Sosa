### Users API ###

from fastapi import APIRouter, HTTPException # API anidada # Habilitar codigo HTTP
from pydantic import BaseModel # mecanismo para crear clases (mas o menos)

# Inicia el server: uvicorn users:app --reload

router = APIRouter()


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


users_list = [User(id=1, name="Kevin", surname="Sosa",age=22),
              User(id=2, name="Keytlin", surname="Sosa",age=26),
              User(id=3, name="Yaque", surname="Felipe",age=56)]


# Creamos un JSON a mano
@router.get("/usersjs")
async def usersjs():  
    return [{"name": "Kevin", "surname": "Sosa","age": 22},
            {"name": "Keytlin", "surname": "Sosa","age": 26},
            {"name": "Yaque", "surname": "Felipe","age": 56}]


# Get: Leer un dato
@router.get("/users")
async def users():
    return users_list

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


# Path: Parte de la url que define que recurso o accion se esta solicitando.

@router.get("/user/{id}")  
async def user(id: int):
    return search_user(id)

# Query: Info adicional que se envia en la url despues del ?
# Sirve para filtrar, ordenar o personalizar la respuesta sin modificar el path.

@router.get("/user/")  
async def user(id: int):
    return search_user(id)


# Post: crear un dato

@router.post("/user/",response_model= User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204,detail="El usuario ya existe") # Codigo HTTP
    else:
        users_list.append(user)
        return user


# Put: modificar un dato

@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


# Delete: Eliminar un dato

@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


