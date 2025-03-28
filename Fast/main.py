from fastapi import FastAPI
from DB.conexion import engine,Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title="Mi primera API",
    description="Blanca estela medina nieves",
    version="1.0.1"
)

Base.metadata.create_all(bind= engine)

#ruta o Endpoint
@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}

app.include_router(routerUsuario)
app.include_router(routerAuth)