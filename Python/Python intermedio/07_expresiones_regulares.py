# Expresiones regulares: diferentes tipos de busquedas en una cadena de texto  

import re

my_string = "Esta es la leccion numero 7: Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"
my_string_copy = "Esta es la leccion numero 7: leccion llamada Expresiones Regulares"

print(re.match("Esta es la leccion",my_string))
print(re.match("Esta es la leccion",my_other_string))
print(re.match("Expresiones Regulares",my_string))      # Si esta en la cadena de texto pero match comienza a buscar desde el principio por lo que sale none

print(re.search("leccion",my_string_copy)) # search busca en cualquier parte de del texto la primera ocurrecia

print(re.findall("leccion",my_string_copy)) # findall listado con la cantidad de ocurrencias

print(re.split(":",my_string_copy)) # split divide el texto a partir del caracter que busque

print(re.sub("leccion","LECCION",my_string_copy)) # sub sustituye un elemento por otro en la cadena de texto

# Patrones propios

patron = r'[a-e]' # lista de todos los caracteres de a la e
print(re.findall(patron,my_string_copy))
print(re.search(patron,my_string_copy))



