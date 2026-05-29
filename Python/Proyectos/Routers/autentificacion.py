from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from Auxiliar.funciones import buscar_usuario_BD, verificar_password,crear_access_token 
from DB.DB import conexion

router = APIRouter()


# Endpoint de login de usuario
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(conexion)):
    user = buscar_usuario_BD(form.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if not verificar_password(form.password, user["contrasena"]):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    access_token = crear_access_token(data = {"sub": user["usuario"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint de login de admin
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
