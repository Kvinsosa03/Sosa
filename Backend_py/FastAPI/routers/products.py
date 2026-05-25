
from fastapi import APIRouter # API anidada 

# Inicia el server: uvicorn products:app --reload

router = APIRouter(prefix="/products", # path por defecto
                   tags=["products"], # para separar en la documentacion
                   responses={404:{"message":"No encontrado"}})

@router.get("/")
async def products():
    return ["Producto 1","Producto 2","Producto 3","Producto 4"]

products_list = ["Producto 1","Producto 2","Producto 3","Producto 4"]

@router.get("/{id}")
async def products(id: int):
    return products_list[id]


