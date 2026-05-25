from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from typing import Optional
from datetime import date, time
from DB.DB import conexion

router = APIRouter()

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

# Modelos de usuario
class User(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str
    disable: bool

# Modelo de reserva
class Reserva(BaseModel):
    id_restaurant: int
    nombre: str
    fecha: date
    horario: time
    comensales: int
    alergias: Optional[str] = None

# Buscar usuario en BD
def buscar_usuario_BD(usuario: str, db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user WHERE usuario = %s;", (usuario,))
    result = cursor.fetchone()   
    cursor.close()
    return result

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

# Endpoint de login
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(conexion)):
    user = buscar_usuario_BD(form.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if form.password != user["contrasena"]:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return {"access_token": user["usuario"], "token_type": "bearer"}

# Endpoint para obtener datos completos del usuario autenticado
@router.get("/user/me")
async def me(current: dict = Depends(current_user), db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT user.id_user,
               user.usuario, 
               user.nombre, 
               user.apellido, 
               user.email,
               COUNT(reservas.id_reservas) AS reservas
        FROM user
        LEFT JOIN reservas 
        ON user.id_user = reservas.id_user
        WHERE user.id_user = %s
        GROUP BY user.id_user, user.usuario, user.nombre, user.apellido, user.email
    """, (current["id_user"],))
    result = cursor.fetchone()
    if not result:
        cursor.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    cursor.execute("""
        SELECT restaurant.nombre AS restaurant, 
               reservas.comensales, 
               reservas.alergias, 
               reservas.fecha, 
               TIME_FORMAT(reservas.horario, '%H:%i') AS horario
        FROM reservas
        LEFT JOIN restaurant 
        ON restaurant.id_restaurant = reservas.id_restaurant
        WHERE reservas.id_user = %s
    """, (current["id_user"],))
    reservas = cursor.fetchall()
    cursor.close()
    result["Detalles"] = reservas

    return result

# Endpoint para crear reserva del usuario autenticado
@router.post("/reservas")
def crear_reserva(reserva: Reserva, current: dict = Depends(current_user), db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)

    # Obtener capacidad del restaurante
    cursor.execute("SELECT capacidad FROM restaurant WHERE id_restaurant = %s", (reserva.id_restaurant,))
    restaurante = cursor.fetchone()
    if not restaurante:
        cursor.close()
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    capacidad = restaurante["capacidad"]
    # Buscar disponibilidad para ese día
    cursor.execute("""SELECT disponibilidad 
                    FROM disponibilidad_restaurante
                    WHERE id_restaurant = %s AND fecha = %s""", (reserva.id_restaurant, reserva.fecha))
    disp = cursor.fetchone()

    if not disp:
        disponibilidad = capacidad
        cursor.execute("""
            INSERT INTO disponibilidad_restaurante (id_restaurant, fecha, disponibilidad)
            VALUES (%s, %s, %s)
        """, (reserva.id_restaurant, reserva.fecha, capacidad))
    else:
        disponibilidad = disp["disponibilidad"]

    # Comprobar disponibilidad
    if disponibilidad < reserva.comensales:
        cursor.close()
        raise HTTPException(status_code=400, detail="No hay disponibilidad suficiente")

    # Insertar reserva asociada al usuario autenticado
    cursor.execute("""
        INSERT INTO reservas (id_restaurant, id_user, nombre, fecha, horario, comensales, alergias)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        reserva.id_restaurant,
        current["id_user"], 
        reserva.nombre,
        reserva.fecha,
        reserva.horario,
        reserva.comensales,
        reserva.alergias
    ))

    # Actualizar disponibilidad
    nueva_disp = disponibilidad - reserva.comensales
    cursor.execute("""
        UPDATE disponibilidad_restaurante
        SET disponibilidad = %s
        WHERE id_restaurant = %s AND fecha = %s
    """, (nueva_disp, reserva.id_restaurant, reserva.fecha))

    db.commit()
    cursor.close()

    return {"mensaje": "Reserva creada exitosamente", "disponibilidad_restante": nueva_disp}
