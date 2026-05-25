from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import time
from DB.DB import conexion


router = APIRouter()

class Restaurante(BaseModel):
    nombre: str
    open: time
    close: time
    ubicacion: Optional[str] = None
    categoria: Optional[str] = None
    capacidad: int

# Obtener datos de restaurantes    
@router.get("/restaurantes")
async def leer_restaurantes(db = Depends(conexion)):
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
    

# Crea restaurante 
@router.post("/restaurante")
async def crear_restaurante(objet: Restaurante,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO restaurant (nombre,open,close,ubicacion,categoria,capacidad) VALUES (%s,%s,%s,%s,%s,%s)""",
                   (objet.nombre, objet.open, objet.close,objet.ubicacion, objet.categoria, objet.capacidad,  ))
    db.commit()
    cursor.close()
    return {"message":"Restaurante creado"}  

# Modificar un usuario
@router.put("/restaurante/{id}")
async def modificar_user(id: int, datos: Restaurante, db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("""UPDATE restaurant SET nombre = %s, open = %s, close = %s, ubicacion = %s, categoria = %s, capacidad = %s WHERE id_restaurant = %s""",
                   (datos.nombre, datos.open, datos.close, datos.ubicacion, datos.categoria, datos.capacidad, id))
    db.commit()
    cursor.close()
    return {"message":"Restaurante actualizado"}

# Eliminar un usuario
@router.delete("/restaurante/{id}")
async def eliminar_restaurante(id: int,db = Depends(conexion)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM restaurant WHERE id_restaurant = %s;",(id,))
    db.commit()
    cursor.close()
    return {"message":"Restaurante eliminado"}



