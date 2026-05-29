from fastapi import APIRouter, Depends, HTTPException
from Auxiliar.funciones import current_user, verificar_password, encriptar_password
from Auxiliar.modelos import User, UserUpdate, Reserva
from datetime import date
from DB.DB import conexion

router = APIRouter()

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

# Endpoint para modificar datos del usuario autenticado
@router.put("/user/me")
async def modificar_user(datos: UserUpdate,current: dict = Depends(current_user), db = Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("SELECT contrasena FROM user WHERE id_user = %s", (current["id_user"],))
    user_db = cursor.fetchone()
    if not user_db:
        cursor.close()
        raise HTTPException(status_code=404, detail= "Usuario no encontrado")
    
    if not verificar_password(datos.contrasena_actual, user_db["contrasena"]):
        cursor.close()
        raise HTTPException(status_code= 400, detail= "Contrasena actual incorrecta")
    
    nueva_contrasena_encriptada = encriptar_password(datos.contrasena_nueva)
    
    cursor.execute("""UPDATE user SET usuario = %s, nombre = %s, apellido = %s, email = %s, contrasena = %s WHERE id_user = %s""",
                   (datos.usuario,datos.nombre, datos.apellido, datos.email, nueva_contrasena_encriptada ,current["id_user"]))
    db.commit()
    cursor.close()
    return {"message":"Usuario actualizado"}

# Crear nuevo usuario
@router.post("/user")
async def crear_user(user: User,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO user (usuario,nombre,apellido,email,contrasena) VALUES (%s,%s,%s,%s,%s)""",
                   (user.usuario, user.nombre, user.apellido, user.email, encriptar_password(user.contrasena)))
    db.commit()
    cursor.close()
    return {"message":"Usuario creado"}

# Endpoint para consultar disponibilidad
@router.get("/disponibilidad/{id_restaurant}/{fecha}")
def consultar_disponibilidad(id_restaurant: int, fecha: date, db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)

    # Verificar que el restaurante exista
    cursor.execute("SELECT nombre, open, close FROM restaurant WHERE id_restaurant = %s", (id_restaurant,))
    restaurante = cursor.fetchone()
    if not restaurante:
        cursor.close()
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    # Consultar todas las horas de disponibilidad para esa fecha
    cursor.execute("""
        SELECT horario, disponibilidad 
        FROM disponibilidad_restaurante
        WHERE id_restaurant = %s AND fecha = %s
        ORDER BY horario ASC
    """, (id_restaurant, fecha))
    disponibilidades = cursor.fetchall()
    cursor.close()

    if not disponibilidades:
        raise HTTPException(status_code=404, detail="No hay disponibilidad inicializada para esa fecha")

    return {
        "restaurante": restaurante["nombre"],
        "fecha": str(fecha),
        "horario_apertura": str(restaurante["open"]),
        "horario_cierre": str(restaurante["close"]),
        "disponibilidades": disponibilidades
    }

# Endpoint para crear reserva del usuario autenticado
@router.post("/reservas")
def crear_reserva(reserva: Reserva, current: dict = Depends(current_user), db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)

    # Obtener capacidad y horarios del restaurante
    cursor.execute("SELECT capacidad, open, close FROM restaurant WHERE id_restaurant = %s", (reserva.id_restaurant,))
    restaurante = cursor.fetchone()
    if not restaurante:
        cursor.close()
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    # Validar que la hora solicitada esté dentro del horario de apertura
    if not (restaurante["open"] <= reserva.horario <= restaurante["close"]):
        cursor.close()
        raise HTTPException(status_code=400, detail="Horario fuera del rango de apertura")

    # Buscar disponibilidad para esa fecha y hora (ya inicializada)
    cursor.execute("""SELECT disponibilidad 
                      FROM disponibilidad_restaurante
                      WHERE id_restaurant = %s AND fecha = %s AND horario = %s""",
                   (reserva.id_restaurant, reserva.fecha, reserva.horario))
    disp = cursor.fetchone()

    if not disp:
        cursor.close()
        raise HTTPException(status_code=404, detail="Disponibilidad no inicializada para esa fecha y hora")

    disponibilidad = disp["disponibilidad"]

    # Comprobar disponibilidad
    if disponibilidad < reserva.comensales:
        cursor.close()
        raise HTTPException(status_code=400, detail="No hay disponibilidad suficiente en esa hora")

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

    # Actualizar disponibilidad de esa hora
    nueva_disp = disponibilidad - reserva.comensales
    cursor.execute("""
        UPDATE disponibilidad_restaurante
        SET disponibilidad = %s
        WHERE id_restaurant = %s AND fecha = %s AND horario = %s
    """, (nueva_disp, reserva.id_restaurant, reserva.fecha, reserva.horario))

    db.commit()
    cursor.close()

    return {
        "mensaje": "Reserva creada exitosamente",
        "fecha": str(reserva.fecha),
        "hora": str(reserva.horario),
        "disponibilidad_restante": nueva_disp
    }
    