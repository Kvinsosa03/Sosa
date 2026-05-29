from pydantic import BaseModel
from typing import Optional
from datetime import date, time

# Modelos de usuario
class User(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str
    contrasena: str

class UserUpdate(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str
    contrasena_actual: str
    contrasena_nueva: str
    
# Modelo de reserva
class Reserva(BaseModel):
    id_restaurant: int
    nombre: str
    fecha: date
    horario: time
    comensales: int
    alergias: Optional[str] = None
    
# Modelo de restaurante    
class Restaurante(BaseModel):
    nombre: str
    open: time
    close: time
    ubicacion: Optional[str] = None
    categoria: Optional[str] = None
    capacidad: int
 