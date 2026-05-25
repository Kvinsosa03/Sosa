from fastapi import APIRouter, Depends
from pydantic import BaseModel
from DB.DB import conexion

router = APIRouter()

class User(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str
    contrasena: str

# Obtener datos de usuarios 
@router.get("/users")
async def leer_users(db = Depends(conexion)):
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
@router.get("/users/{id}")  
async def leer_user(id: int,db = Depends(conexion)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""SELECT  user.id_user,
                            user.usuario, 
                            user.nombre, 
                            user.apellido, 
                            user.email,
                            user.contrasena, 
                            COUNT(reservas.id_reservas) AS reservas
                    FROM user
                    LEFT JOIN reservas 
                    ON user.id_user = reservas.id_user
                    WHERE user.id_user = %s
                    GROUP BY user.id_user, user.nombre, user.apellido, user.email""", (id,))
    result = cursor.fetchone()
    
    if not result:
        cursor.close()
        return {"error": "No se ha encontrado el usuario"}
    
    cursor.execute("""SELECT restaurant.nombre AS restaurant, 
                            reservas.comensales, 
                            reservas.alergias, 
                            reservas.fecha, 
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
    
# Crear un usuario
@router.post("/user")
async def crear_user(user: User,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO user (usuario,nombre,apellido,email,contrasena) VALUES (%s,%s,%s,%s,%s)""",
                   (user.usuario, user.nombre, user.apellido, user.email, user.contrasena))
    db.commit()
    cursor.close()
    return {"message":"Usuario creado"}

# Modificar un usuario
@router.put("/user/{id}")
async def modificar_user(id: int, datos: User, db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""UPDATE user SET usuario = %s, nombre = %s, apellido = %s, email = %s, contrasena = %s WHERE id_user = %s""",
                   (datos.usuario,datos.nombre, datos.apellido, datos.email, datos.contrasena,id))
    db.commit()
    cursor.close()
    return {"message":"Usuario actualizado"}

# Eliminar un usuario
@router.delete("/user/{id}")
async def eliminar_user(id: int,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM user WHERE id_user = %s;",(id,))
    db.commit()
    cursor.close()
    return {"message":"Usuario eliminado"}

