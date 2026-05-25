### Users_db API ###

from fastapi import APIRouter, HTTPException, status
from db.models.users import User
from db.schemas.user import user_schemas, users_schemas
from db.client import db_clint
from bson import ObjectId

router = APIRouter()


def search_user(field: str, key):
    try:
        user = db_clint.users.find_one({field: key})
        new_user = User(**user_schemas(user))
        return new_user
    except:
        return {"error": "No se ha encontrado el usuario"}

 
# Post: crear un dato en base de datos
@router.post("/userdb/",response_model= User, status_code = status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email",user.email)) == User:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "El usuario ya existe") 
   
    user_dict = dict(user)
    del user_dict["id"]
   
    id = db_clint.users.insert_one(user_dict).inserted_id
    
    new_user = user_schemas(db_clint.users.find_one({"_id":id})) 
    
    return User(**new_user)


# Get: obtener datos de la base de datos
@router.get("/usersdb", response_model = list[User])
async def users():
    return users_schemas(db_clint.users.find())

@router.get("/userdb/{id}")  
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.get("/userdb/")  
async def user(id: str):
    return search_user("_id", ObjectId(id))


# Delete: eliminar un dato de base de datos
@router.delete("/userdb/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_clint.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
    
    
# Put: modificar un dato de base de datos
@router.put("/userdb/",response_model= User)
async def user(user: User):
    
    user_dict = dict(user)
    del user_dict["id"]
    
    try:
        
        db_clint.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
        
    except:
        return {"error": "No se ha actualizado el usuario"}


    return search_user("_id", ObjectId(user.id))


