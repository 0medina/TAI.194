#creacion del modelo con parametros 
#importar librerias

from pydantic import BaseModel,Field

class modelVehiculo(BaseModel):
    año: int = Field(..., gt=4, description="El año debe de tener 4 digitos.")
    modelo: str = Field(..., min_length=4, max_length=25, description="El modelo debe de contra con almenos 4 letras y un maximo de 25 ")
    placa: str = Field(..., min_length=1, max_lenght=10, description="La placa debe de contar con maximo 10 digitos o letras.")