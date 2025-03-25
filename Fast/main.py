from fastapi import FastAPI,HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional,List # define para que los caracteres en las api sean opcionales o no
from modelsPydantic import modelUsuario, modelAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
    title="Mi primera API",
    description="Blanca estela medina nieves",
    version="1.0.1"
)

Base.metadata.create_all(bind= engine)

    
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
        return JSONResponse(content={"Token": token})
    else:
        return {"Aviso":"Usuario no autorizado"}
            

#Endpoint CONSULTA TODOS
@app.get('/todosUsuario',tags=['Operaciones CRUD'])
def leer():
   db=Session()
   try:
       consulta=db.query(User).all()
       return JSONResponse(content= jsonable_encoder(consulta))
   
   except Exception as e:
       db.rollback()
       return JSONResponse(status_code=500, content={"message": "No fue posible consultar", "Error": str(e)})
   finally:
       db.close()
   
   
#Endpoint POST
@app.post('/usuarios/',response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    db=Session()
    try:
        db.add( User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"message": "usuario Guardado", "usuario": usuario.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Mo fue posible guardar", "Error": str(e)})
    
    finally:
        db.close()       
        
#Endpoint para actualizar
@app.put('/usuarios/{id}' ,response_model=modelUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario): 
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404, detail="El usuario no existe")

#endopint busca para borrar 
@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int): 
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
             usuarios.pop(index)
             return usuarios[index]
    raise HTTPException(status_code=404, detail="El usuario que buscas no existe ")

#Endpoint Para buscar por ID
@app.get('/usuarios/{id}',tags=['Operaciones CRUD'])
def leeruno(id:int):
    db=Session()
    try:
        consulta=db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario mo encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Mo fue posible guardar", "Error": str(e)})
    
    finally:
        db.close()       
        
                                