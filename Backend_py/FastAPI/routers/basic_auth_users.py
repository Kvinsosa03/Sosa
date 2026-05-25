# Mecanismo de autentificacion basico

# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel # mecanismo para crear clases (mas o menos)

# OAuth2PasswordBearer: clase encargada de gestionar la autentificacion (usuario y contrasena) 
# OAuth2PasswordRequestForm: forma en la q se envian al API los criterios de utentificacion 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

# Inicializacion de la API
router = APIRouter()

# Definimos el esquema de seguridadOAuth2
# tokenUrl="login" indica que /login sera el encargado de generar tokens.
OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

# Modelos de usuarios
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool
   
class UsersDB(User):
    password: str
    
# Base de Datos simulada en memoria    
users_db = {
    "Kevin": {
        "username": "Kevin",
        "full_name": "Kevin Sosa",
        "email": "kevinsosa@gmail.com",
        "disable": False,
        "password": "123456"
    },
    "Kevin2": {
        "username": "Kevin2",
        "full_name": "Kevin Sosa 2",
        "email": "kevinsosa2@gmail.com",
        "disable": False,
        "password": "654321"
    }
}

def search_user_db(username: str):
    # devuelve el usuario con contrasena (para validacion interna)
    if username in users_db:
        return UsersDB(**users_db[username])
    
def search_user(username: str):
     # devuelve el usuario sin contrasena (para exponer datos seguros)
    if username in users_db:
        return User(**users_db[username])
        
 
# dependencia: usuario actual   
async def current_user(token: str = Depends(OAuth2)):
    # Busaca el usuario asociado al token recibido
    user = search_user(token)
    if not user:
        # Si no existe, error 401
        raise HTTPException(status_cod = status.HTTP_401_UNAUTHORIZED, 
                            detail = "Credenciales de autentificacion invalida",
                            headers = {"www-Authenticate":"Bearer"})
        
    if user.disable:
        # si el usuario esta desabilitado, error 400
         raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Usuario inactivo")
    return user # Devuelve el usuario valido
      
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Usuario no es correcto")
    
    user = search_user_db(form.username)
    if  not form.password == user.password:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Contasena incorrecta")

    # autentificacion correcta: el sistema devuelve de manera estandar un access_token. 
    # access_token: cadena de caracteres unica y temporal, sirve para autenticar y autorizar solicitudes a recursos protegidos. Se emite tras autentificaion exitosa. 
    return {"access_token": user.username, 
            "token_type": "bearer"
            }
 
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
    


