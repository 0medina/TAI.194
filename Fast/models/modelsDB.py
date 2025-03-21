from DB.conexion import Base
from sqlalchemy import Column, Integer, String  #para importar todos los datos que podemos llegar a usar

class User(Base): #se realiza la conexion a la base de datos 
    __tablename__='tbUser'#primer atributo de la tabla,aqui se declaran las tablas aunque lo mejor es una clase por tabla 
    id= Column(Integer, primary_key=True, autoincrement="auto")
    name= Column(String)
    age= Column(Integer)
    email= Column(String)
    
    