from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db # ruters para anidar APIs
from fastapi.staticfiles import StaticFiles # recursos estaticos (fotos,pdf)

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# Recursos estaticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Iniciar server: uvicorn main:app --reload
# Detener server: CTRL + C

# Url local : http://127.0.0.1.8000
@app.get("/")
async def root():
    return "Hola FastAPI"

# Url local : http://127.0.0.1.8000/url
@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}

# Documentacion con Swagger: http://127.0.0.1.8000/docs
# Documentacion con Redocly: http://127.0.0.1.8000/redoc

# HTTP Status Codes

# 100: information
# 200: successful
# 201: created
# 204: not content
# 300: redirection
# 304: not modified
# 400: client error
# 404: not found
# 500: server error




