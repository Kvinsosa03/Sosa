from fastapi import FastAPI
from Routers import autentificacion,cliente_acciones,admin_acciones
from apscheduler.schedulers.background import BackgroundScheduler
from Auxiliar.funciones import extender_disponibilidad_automatica


app = FastAPI()

# Configurar APScheduler
scheduler = BackgroundScheduler()
# Ejecutar cada día a medianoche
scheduler.add_job(extender_disponibilidad_automatica, "cron", hour=0, minute=0)
scheduler.start()


# Iniciar server: uvicorn conn:app --reload

app.include_router(autentificacion.router)
app.include_router(cliente_acciones.router)
app.include_router(admin_acciones.router)

@app.get("/")
async def root():
    return "Bienvenido"





