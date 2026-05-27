from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from jose import JWSError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from DB.DB import conexion

router = APIRouter()

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

CLAVE_SECRETA = "Todo_correcto"
ALGORITMO = "HS256"
ACCESS_TOKEN_TIME = 15

encriptacion = CryptContext(schemes=["bcrypt"], deprecated = "auto")

# Encriptar contrasena
def encriptar_password(password: str):
    return encriptacion.hash(password)

#Verificar contrasena
def verificar_password(plain_password, hashed_password):
    return encriptacion.verify(plain_password,hashed_password)

# Crear JWT
def crear_access_token(data: dict, exp_delta: timedelta | None = None ):
    to_encode = data.copy()
    expire = datetime.utcnow() + (exp_delta or timedelta(minutes = (ACCESS_TOKEN_TIME)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, CLAVE_SECRETA, algorithm = ALGORITMO)

# Buscar usuario en BD
def buscar_usuario_BD(usuario: str, db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user WHERE usuario = %s;", (usuario,))
    result = cursor.fetchone()   
    cursor.close()
    return result


# Endpoint de login
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(conexion)):
    user = buscar_usuario_BD(form.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if not verificar_password(form.password, user["contrasena"]):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    access_token = crear_access_token(data = {"sub": user["usuario"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login_admin")
async def login_admin(form: OAuth2PasswordRequestForm = Depends(), db=Depends(conexion)):
    user = buscar_usuario_BD(form.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if not verificar_password(form.password, user["contrasena"]):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    if user["rol"] != "admin":
        raise HTTPException(status_code=403, detail="Acceso restringido solo a administradores")
    
    access_token = crear_access_token(data={"sub": user["usuario"], "rol": user["rol"]})
    return {"access_token": access_token, "token_type": "bearer"}
