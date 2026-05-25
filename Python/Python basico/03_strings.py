my_strings = "My strings "
my_other_strings = "My Other strings"

print(my_strings)
print(my_other_strings)

print(my_strings +my_other_strings)
print(len(my_strings)+len(my_other_strings))

salto_de_linea = "Kevin\nSosa"
tabulacion = "\tKevin Sosa"

print(salto_de_linea)
print(tabulacion)

# formateo

name,subname,age = "Kevin","Sosa",22

print("mi nombre es %s %s y mi edad es %d"%(name,subname,age))
print("mi nombre es {} {} y mi edad es {}".format(name,subname,age))
print(f"mi nombre es {name} {subname} y mi edad es {age}")

# desenpaquetado de caracteres 
 
lenguaje = "hola"
a,b,c,d = lenguaje
e = lenguaje [0:3]  # desde elcaracter 0 evitando los caracteres q estan despues del :
f = lenguaje[::-1]  # invertir

print(a)
print(d)
print(b)
print(c)

print(e)
print(f)

# Funciones

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("o"))
print(lenguaje.isnumeric())
print(lenguaje.startswith("ho"))



