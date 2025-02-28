from fastapi import FastAPI,HTTPException
from typing import Optional,List # define para que los caracteres en las api sean opcionales o no
from models import modelUsuario, modelAuth
from genToken import createToken



app = FastAPI(
    title="Mi primera API",
    description="Blanca estela medina nieves",
    version="1.0.1"
)
    
usuarios=[
    {"id":1, "nombre":"estela", "edad":22, "correo":"estela123@gmail.com"},
    {"id":2, "nombre":"Carlos", "edad":20, "correo":"charly34@gmail.com"},
    {"id":3, "nombre":"jose", "edad":21, "correo":"jose13@gmail.com"},
    {"id":4, "nombre":"mario", "edad":22, "correo":"mario14@gmail.com"},
]
#ruta o Endpoint
@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}

#endpoints  para generar tokens
@app.post('/auth', tags=['Autentificacion'])
def auth (credenciales:modelAuth):
    if credenciales.mail == 'estela@example.com' and credenciales.passw == '123456789':
        token:str= createToken(credenciales.model_dump())
        print (token)
        return {"Aviso":"Token generado"}
    else:
        return {"Aviso":"Usuario no cuenta con permiso"}
            

#Endpoint CONSULTA TODOS
@app.get('/todosUsuario', response_model=list[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return  usuarios 

#Endpoint POST
@app.post('/usuarios/',response_model=list[modelUsuario], tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr['id'] == usuario.id :
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuarios

#Endpoint para actualizar
@app.put('/usuarios/{id}' ,response_model=modelUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario): 
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404, detail="El usuario no existe")

@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int): 
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
             usuarios.pop(index)
             return usuarios[index]
    raise HTTPException(status_code=404, detail="El usuario que buscas no existe ")

