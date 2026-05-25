import mysql.connector
from fastapi import Depends
def conexion():
   db=mysql.connector.connect(
        host= "127.0.0.1",
        port= 3306,
        database = "agencia",
        user = "root",
        password ="Root1234"
   )  
   try:
       yield db
   finally:
       db.close()
   
       
