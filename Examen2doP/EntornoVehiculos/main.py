#crear una API para el registro de vehiculos: Modelo, Año, Placa
#importar librerias 
from fastapi import FastAPI
from pydantic import BaseModel
from models import modelVehiculo
#bienvenida
app = FastAPI(
    title="API de registro de vehiculos por medina nieves blanca estela S194",
    description="API para el registro y gestión de vehículos",
    version="1.0.0"
)

#base de datos ficticia 
db = {
    "vehiculo": [
        {"id": 1, "modelo": "Toyota", "año": 2020, "placa": "ABC123"},
        {"id": 2, "modelo": "Honda", "año": 2021, "placa": "DEF456"},
        {"id": 3, "modelo": "Nissan", "año": 2019, "placa": "GHI789"},
    ]
}

#endpoint get para obtener todo los vehiculos
@app.get("/vehiculo/{id}", tags=["Vehiculo"])
def obtener_vehiculo_por_id(id: int):
    for vehiculo_db in db.vehiculo:
        if vehiculo_db["id"] == id:
            return vehiculo_db

#endpoint para guardar vehiculos
@app.post("/vehiculo", tags=["Vehiculo"])
def guardar_vehiculo(vehiculo: modelVehiculo):
    db.vehiculo.insert_one(vehiculo.dict())
    return {"message": "Vehiculo guardado exitosamente"}

#endpoint para actualizar un vehiculo
@app.put("/vehiculo/{id}", tags=["Vehiculo"])
def actualizar_vehiculo(id: int, vehiculo: modelVehiculo):
    for vehiculo_db in db.vehiculo:
        if vehiculo_db["id"] == id:
            vehiculo_db.update(vehiculo.dict())
            return {"message": "Vehiculo actualizado exitosamente"}
    
