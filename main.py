from peewee import *
import pymysql
import datetime

db = MySQLDatabase(
    'Empresa',
    user='usuario',
    password='hola',
    host='localhost',
    port=3306
)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    dni = CharField (max_length=9, primary_key=True)
    nombre = CharField(max_length=20)
    apellido = CharField(max_length=40)

    class Meta:
        table_name = "clientes"

class Empleado(BaseModel):
    dni = CharField (max_length=9, primary_key=True)
    num_articulos = IntegerField (default=0)
    acceso = DateTimeField(default=datetime.now())

    class Meta:
        table_name = "ventas"



if __name__ == '__main__':
    pass