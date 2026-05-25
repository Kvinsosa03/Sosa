# Mecanismo de autentificacion jwt

# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel # mecanismo para crear clases (mas o menos)
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# OAuth2PasswordBearer: clase encargada de gestionar la autentificacion (usuario y contrasena) 
# OAuth2PasswordRequestForm: forma en la q se envian al API los criterios de utentificacion 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "1a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16p17q18r19s20t"

router = APIRouter()

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes = ["bcrypt"])

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
        "password": "$2a$12$5TgS90BLivBsbe2hddVouuTOEAouU5QkOB2svi2lc3hV5YdOlgq4O"
    },
    "Kevin2": {
        "username": "Kevin2",
        "full_name": "Kevin Sosa 2",
        "email": "kevinsosa2@gmail.com",
        "disable": False,
        "password": "$2a$12$krSy5SFXEo5C1IbVe180YezOBjMl5Q1xcS1ojShNII/iLScrZuD.a"
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



async def auth_user(token: str = Depends(OAuth2)):
    
    exception = HTTPException(  status_code = status.HTTP_401_UNAUTHORIZED, 
                                detail = "Credenciales de autentificacion invalida",
                                headers = {"www-Authenticate":"Bearer"})

    
    try:
        username = jwt.decode(token,SECRET,algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
        
    except JWTError:
        raise exception
    
    return search_user(username)
    
            
async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        # si el usuario esta desabilitado, error 400
         raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Usuario inactivo")
    return user # Devuelve el usuario valido


@router.post("/loginjwt")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Usuario no es correcto")
    
    user = search_user_db(form.username)
    
    if  not crypt.verify(form.password,user.password):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "Contasena incorrecta")

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    
    access_token = {"sub": user.username, 
                    "Exp": int(expire.timestamp())}

    # autentificacion correcta: el sistema devuelve de manera estandar un access_token. 
    # access_token: cadena de caracteres unica y temporal, sirve para autenticar y autorizar solicitudes a recursos protegidos. Se emite tras autentificaion exitosa. 
    return {"access_token": jwt.encode(access_token,SECRET, algorithm=ALGORITHM), 
            "token_type": "bearer"
            }
    
    
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user