# tipos de errores

# SyntaxError
# print "Hola comunidad" # error
print("Hola comunidad")

# NameError
# print(nombre) # Error: no esta definda la variable
nombre= "Kevin"
print(nombre)

# IndexError
my_list = ["python", "swift", "kotlin", "dart", "javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Error: lista fuera de rango

# ModuleNotFoundError
# import maths # Error
import math

# AttibuteError
# print(math.PI) # Error
print(math.pi)

# KeyErrror
my_other_dict = {"Nombre":"Kevin","Apellido":"Sosa","Edad":22, 1:"Python"}
print(my_other_dict["Nombre"])
# print(my_other_dict["Apelido"]) # Error

# TypeError
# print(my_list[nombre]) # Error
print(my_list[0])

# ImportError
# from math import PI # Error
from math import pi
print(pi)


