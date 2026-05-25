# ficheros

import os

txt = open("Python intermedio/my_file.txt","r+") # r: leer w:escribir

#txt.write("Mi nombre es Kevin\nMi apellido es Sosa\n22 anos\nmi lenguaje preferido es C")

print(txt.read())         # leer fichero
print(txt.readline())     # leer linea del fichero
print(txt.readline())    # leer las lineas en una lista
for i in txt.readlines(): # leer las lineas una debajo de otra
    print(i)

txt.write("\nPero tambien me gusta Python")   
print(txt.readline())

txt.close()

# os.remove("Python intermedio/my_file.txt") # borrar
 
# .json file

import json
 
json_file = open("Python intermedio/my_file.json","w+") # crear fichero de cero

json_test ={
    "nombre":"Kevin",
    "apellido":"Sosa",
    "edad":22 ,
    "lenguaje":"Python"}

json.dump(json_test,json_file,indent=2) #dump: escibir en json_fie  #indet: te organiza el finero 

json_file.close()  

# .csv file

import csv
 
# .xml file

import xml
          