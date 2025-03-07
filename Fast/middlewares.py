from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from genToken import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        
        if not isinstance(data, dict): #verifica si es un diccionario valido
            raise HTTPException(status_code=401, detail="formato de token no valido")
        
        if data.get('mail') != 'estela@example.com': #usa .get() para evitar kerError
            raise HTTPException(status_code=403, detail="credenciales no validos")