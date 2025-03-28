from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

##CRUD DE USUARIOS
#Endpoint CONSULTA TODOS
@routerUsuario.get('/todosUsuario',tags=['Operaciones CRUD'])
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
   
#Endpoint para guardar post
@routerUsuario.post('/usuarios/',response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if usuario:
            for key, value in usuarioActualizado.model_dump().items():
                setattr(usuario, key, value)
            db.commit()
            return JSONResponse(status_code=201, content={"message": "usuario actualizado", "usuario": usuario.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Mo fue posible actualizar", "Error": str(e)})
    
    finally:
        db.close()  
        
#endopint busca para eliminar 
@routerUsuario.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id: int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return JSONResponse(status_code=201, content={"message": "usuario eliminado", "usuario": usuario.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Mo fue posible eliminar", "Error": str(e)})
    
    finally:
        db.close() 

#Endpoint Para buscar por ID
@routerUsuario.get('/usuarios/{id}',tags=['Operaciones CRUD'])
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