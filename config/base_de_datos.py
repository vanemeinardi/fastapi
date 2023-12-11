import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

fichero = "../datos.sqlite"
# leemos el directorio actual del archivo de bd
directorio = os.path.dirname(os.path.realpath(__file__))
# direccion bd, uniendo las 2 var anteriores
ruta = f"sqlite:///{os.path.abspath(os.path.join(directorio, fichero))}"

#ruta = f"sqlite:///{os.path.join(directorio,fichero)}"
# creamos el motor 
print("Ruta de la base de datos:", ruta)

motor = create_engine(ruta, echo=True)
# creamos la sesion pasandole el motor 
sesion = sessionmaker(autocommit=False, autoflush=False,bind=motor)
# crear base para manejar las tablas de bd
base = declarative_base()