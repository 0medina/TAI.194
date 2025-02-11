from fastapi import FastAPI,HTTPException
from typing import Optional # define para que los caracteres en las api sean opcionales o no

app = FastAPI(
    title="Mi primera API",
    description="Blanca estela medina nieves",
    version="1.0.1"
)
usuarios=[
    {"id":1, "nombre":"estela", "edad":22},
    {"id":2, "nombre":"Carlos", "edad":20},
    {"id":3, "nombre":"jose", "edad":21},
    {"id":4, "nombre":"mario", "edad":22},
]
#ruta o Endpoint
@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}

#Endpoint CONSULTA TODOS
@app.get('/todosUsuario', tags=['Operaciones CRUD'])
def leer():
    return {'Usuarios Registrados' : usuarios }

#Endpoint POST
@app.post('/usuarios/', tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr['id'] == usuario.get("id"):
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuarios

#Endpoint para actualizar
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:dict): 
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=404, detail="El usuario no existe")