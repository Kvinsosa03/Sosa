from fastapi import APIRouter, Depends, HTTPException
from Auxiliar.funciones import current_admin, encriptar_password, inicializar_disponibilidad
from Auxiliar.modelos import User, Restaurante
from datetime import date
from typing import List
from DB.DB import conexion

router = APIRouter()

# Obtener datos de usuarios 
@router.get("/admin/users")
async def leer_users(current: dict = Depends(current_admin),db = Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT  user.id_user,
                            user.usuario, 
                            user.nombre, 
                            user.apellido, 
                            user.email, 
                            COUNT(reservas.id_reservas) AS reservas
                    FROM user
                    LEFT JOIN reservas 
                    ON user.id_user = reservas.id_user
                    GROUP BY user.id_user, user.nombre, user.apellido, user.email;""")
    
    result = cursor.fetchall()
    cursor.close()
    
    return result


# Obtener datos de usuario especifico
@router.get("/admin/users/{id}")  
async def leer_user(id: int,current: dict = Depends(current_admin),db = Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT  user.id_user,
                            user.usuario, 
                            user.nombre, 
                            user.apellido, 
                            user.email, 
                            COUNT(reservas.id_reservas) AS reservas
                    FROM user
                    LEFT JOIN reservas 
                    ON user.id_user = reservas.id_user
                    WHERE user.id_user = %s
                    GROUP BY user.usuario, user.id_user, user.nombre, user.apellido, user.email""", (id,))
    result = cursor.fetchone()
    
    if not result:
        cursor.close()
        return {"error": "No se ha encontrado el usuario"}
    
    cursor.execute("""SELECT restaurant.nombre AS restaurant, 
                            reservas.comensales, 
                            reservas.alergias, 
                            reservas.fecha,
                            reservas.estado, 
                            TIME_FORMAT(`horario`, '%H:%i') AS horario
                    FROM reservas
                    LEFT JOIN restaurant 
                    ON restaurant.id_restaurant = reservas.id_restaurant
                    WHERE reservas.id_user = %s """,
                    (id,))
    
    reservas = cursor.fetchall()
    cursor.close()
    
    result["Detalles"] = reservas
    
    return result

# Crear nuevo usuario
@router.post("/user")
async def crear_user(user: User,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO user (usuario,nombre,apellido,email,contrasena) VALUES (%s,%s,%s,%s,%s)""",
                   (user.usuario, user.nombre, user.apellido, user.email, encriptar_password(user.contrasena)))
    db.commit()
    cursor.close()
    return {"message":"Usuario creado"}

# Eliminar un usuario
@router.delete("/admin/users/{id}")
async def eliminar_user(id: int,current: dict = Depends(current_admin),db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("UPDATE reservas SET estado = 'cancelada' WHERE id_user = %s", (id,))
    cursor.execute("DELETE FROM user WHERE id_user = %s;",(id,))
    db.commit()
    cursor.close()
    return {"message":"Usuario eliminado"}

# Obtener datos de restaurantes    
@router.get("/admin/restaurantes")
async def leer_restaurantes(current: dict = Depends(current_admin),db = Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT restaurant.nombre, 
                            TIME_FORMAT(`open`, '%H:%i') AS open,
                            TIME_FORMAT(`close`, '%H:%i') AS close, 
                            restaurant.ubicacion,
                            restaurant.categoria,
                            restaurant.capacidad
                        FROM restaurant""")
    result = cursor.fetchall()
    
    limpiar_result = []
    for i in result:
        i = {k: v for k, v in i.items() if v is not None}
        limpiar_result.append(i)

    cursor.close()
    return limpiar_result

# Endpoint para crear restaurante con disponibilidad inicializada
@router.post("/admin/restaurante")
async def crear_restaurante(restaurante: Restaurante,current: dict = Depends(current_admin), db=Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO restaurant (nombre, open, close, ubicacion, categoria, capacidad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (restaurante.nombre, restaurante.open, restaurante.close, restaurante.ubicacion, restaurante.categoria, restaurante.capacidad))
    db.commit()
    id_restaurant = cursor.lastrowid
    cursor.close()

    inicializar_disponibilidad(id_restaurant, restaurante.capacidad, restaurante.open, restaurante.close, dias=30, db=db)

    return {"message": "Restaurante creado con disponibilidad inicializada para 30 días", "id_restaurant": id_restaurant}

# Modificar datos de un restaurante
@router.put("/admin/restaurante/{id}")
async def modificar_restaurante(id: int, datos: Restaurante,current: dict = Depends(current_admin), db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""UPDATE restaurant SET nombre = %s, open = %s, close = %s, ubicacion = %s, categoria = %s, capacidad = %s WHERE id_restaurant = %s""",
                   (datos.nombre, datos.open, datos.close, datos.ubicacion, datos.categoria, datos.capacidad, id))
    db.commit()
    cursor.close()
    return {"message":"Restaurante actualizado"}

# Eliminar un restaurante
@router.delete("/admin/restaurante/{id}")
async def eliminar_restaurante(id: int,current: dict = Depends(current_admin),db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM restaurant WHERE id_restaurant = %s;",(id,))
    db.commit()
    cursor.close()
    return {"message":"Restaurante eliminado"}


# Endpoint para cerrar x dias un restaurante
@router.put("/admin/restaurante/cerrar/{id}")
async def cerrar_restaurante(
    id: int,
    dias: List[date], 
    current: dict = Depends(current_admin),
    db=Depends(conexion)
):
    cursor = db.cursor(dictionary=True)

    # Verificar que el restaurante exista
    cursor.execute("SELECT id_restaurant FROM restaurant WHERE id_restaurant = %s", (id,))
    restaurante = cursor.fetchone()
    if not restaurante:
        cursor.close()
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    placeholders = ",".join(["%s"] * len(dias))
    
    # Eliminar disponibilidades de esos días
    cursor.execute(f"DELETE FROM disponibilidad_restaurante WHERE id_restaurant = %s AND fecha IN ({placeholders})" ,[id] + dias)

    # Marcar reservas como canceladas en esos días
    cursor.execute(f" UPDATE reservas SET estado = 'cancelada' WHERE id_restaurant = %s AND fecha IN ({placeholders})",[id] + dias)

    db.commit()
    cursor.close()

    return {
        "message": f"Restaurante {id} cerrado en las fechas indicadas",
        "fechas_canceladas": [str(d) for d in dias]
    }


# Endpoint para consultar disponibilidad
@router.get("/disponibilidad_diaria/{id_restaurant}/{fecha}")
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
    
from fastapi import APIRouter, Depends, HTTPException
from datetime import date, timedelta
from DB.DB import conexion

router = APIRouter()


# Endpoint para consultar calendario
@router.get("/disponibilidad/calendario/{id_restaurant}")
def consultar_calendario_30dias(id_restaurant: int, db=Depends(conexion)):
    cursor = db.cursor(dictionary=True)

    # Verificar que el restaurante exista
    cursor.execute("SELECT nombre, open, close FROM restaurant WHERE id_restaurant = %s", (id_restaurant,))
    restaurante = cursor.fetchone()
    if not restaurante:
        cursor.close()
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    # Calcular rango de fechas: hoy + 30 días
    inicio = date.today()
    fin = inicio + timedelta(days=30)

    # Consultar disponibilidades en ese rango
    cursor.execute("""
        SELECT fecha, horario, disponibilidad
        FROM disponibilidad_restaurante
        WHERE id_restaurant = %s 
          AND fecha BETWEEN %s AND %s
        ORDER BY fecha ASC, horario ASC
    """, (id_restaurant, inicio, fin))
    disponibilidades = cursor.fetchall()
    cursor.close()

    # Agrupar por fecha
    calendario = {}
    for d in disponibilidades:
        fecha_str = str(d["fecha"])
        if fecha_str not in calendario:
            calendario[fecha_str] = {
                "estado": "abierto",
                "horario_apertura": str(restaurante["open"]),
                "horario_cierre": str(restaurante["close"]),
                "horarios": []
            }
        calendario[fecha_str]["horarios"].append({
            "horario": str(d["horario"]),
            "disponibilidad": d["disponibilidad"]
        })

    # Marcar días sin disponibilidad como cerrados
    dia_actual = inicio
    while dia_actual <= fin:
        fecha_str = str(dia_actual)
        if fecha_str not in calendario:
            calendario[fecha_str] = {
                "estado": "cerrado",
                "horario_apertura": str(restaurante["open"]),
                "horario_cierre": str(restaurante["close"]),
                "horarios": []
            }
        dia_actual += timedelta(days=1)

    return {
        "restaurante": restaurante["nombre"],
        "desde": str(inicio),
        "hasta": str(fin),
        "calendario": calendario
    }
    
