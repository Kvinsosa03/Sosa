# loops

my_condicion = 0

while my_condicion < 10:
    print(my_condicion)
    my_condicion += 2
else:
    print("Mi concion es igual o mayor que 10")

print("La ejecucion continua")

while my_condicion < 20:
    my_condicion += 2
    if my_condicion == 16:
        print("Es igual a 16")
        break
    print(my_condicion)
        
print("La ejecucion continua")

my_lista = [35, 24, 62, 52, 30, 30, 17]

for element in my_lista:
    print(element)
    
    