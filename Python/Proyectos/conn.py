
from fastapi import FastAPI
from Routers import users,restaurant,autentificacion


app = FastAPI()

# Iniciar server: uvicorn conn:app --reload

app.include_router(users.router)
app.include_router(restaurant.router)
app.include_router(autentificacion.router)

@app.get("/")
async def root():
    return "Bienvenido"





