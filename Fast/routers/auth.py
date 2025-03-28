from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from genToken import createToken
from fastapi import APIRouter

routerAuth= APIRouter()

#endpoints  para generar tokens
@routerAuth.post('/auth', tags=['Autentificacion'])
def auth (credenciales:modelAuth):
    if credenciales.mail == 'estela@example.com' and credenciales.passw == '123456789':
        token:str= createToken(credenciales.model_dump())
        print (token)
        return JSONResponse(content={"Token": token})
    else:
        return {"Aviso":"Usuario no autorizado"}