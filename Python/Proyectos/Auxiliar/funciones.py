from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError 
from datetime import time, date, timedelta, datetime
from DB.DB import conexion

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

CLAVE_SECRETA = "Todo_correcto"
ALGORITMO = "HS256"
ACCESS_TOKEN_TIME = 30

encriptacion = CryptContext(schemes=["bcrypt"], deprecated = "auto")

# Dependencia: admin    
async def current_admin(token: str = Depends(OAuth2), db=Depends(conexion)):
    try:
        payload = jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITMO])
        username: str = payload.get("sub")
        role: str = payload.get("rol")
        if username is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    # Buscar usuario en BD
    user = buscar_usuario_BD(username, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso restringido"
        )

    return user


# Dependencia: usuario actual
async def current_user(token: str = Depends(OAuth2), db=Depends(conexion)):
    user = buscar_usuario_BD(token, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas")
    if user["disable"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

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

# Función automática para extender disponibilidad
def extender_disponibilidad_automatica():
    db = conexion()
    cursor = db.cursor(dictionary=True)

    # Obtener todos los restaurantes
    cursor.execute("SELECT id_restaurant, capacidad, open, close FROM restaurant")
    restaurantes = cursor.fetchall()

    for r in restaurantes:
        # Buscar última fecha inicializada
        cursor.execute("SELECT MAX(fecha) AS ultima_fecha FROM disponibilidad_restaurante WHERE id_restaurant = %s", (r["id_restaurant"],))
        ultima = cursor.fetchone()

        if ultima and ultima["ultima_fecha"]:
            fecha_inicio = ultima["ultima_fecha"] + timedelta(days=1)
        else:
            fecha_inicio = date.today()

        # Inicializar un día más de disponibilidad
        hora = r["open"]
        while hora <= r["close"]:
            cursor.execute("""
                INSERT INTO disponibilidad_restaurante (id_restaurant, fecha, horario, disponibilidad)
                VALUES (%s, %s, %s, %s)
            """, (r["id_restaurant"], fecha_inicio, hora, r["capacidad"]))
            hora = (datetime.combine(fecha_inicio, hora) + timedelta(hours=1)).time()

    db.commit()
    cursor.close()
    db.close()
    print("Disponibilidad extendida automáticamente")
    

# Inicializar disponibilidad
def inicializar_disponibilidad(id_restaurant: int, capacidad: int, hora_apertura: time, hora_cierre: time, dias: int, db=Depends(conexion)):
    cursor = db.cursor()
    hoy = date.today()
    for d in range(dias):
        fecha = hoy + timedelta(days=d)
        hora = hora_apertura
        while hora <= hora_cierre:
            cursor.execute("""
                INSERT INTO disponibilidad_restaurante (id_restaurant, fecha, horario, disponibilidad)
                VALUES (%s, %s, %s, %s)
            """, (id_restaurant, fecha, hora, capacidad))
            hora = (datetime.combine(fecha, hora) + timedelta(hours=1)).time()
    db.commit()
    cursor.close()
    
