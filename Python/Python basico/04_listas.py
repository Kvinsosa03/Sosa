# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,22,52,30,30,22]

print(my_list)
print(len(my_list))

my_other_list = [22,1.70,"Kevin",'Sosa']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_list.count(30))        # numero de frcuencias de un valor

age, altura, name, subname = my_other_list
print(name)

print(my_list + my_other_list)
 
my_other_list.append("CUJAE")   # Anadir elemento al final
print(my_other_list)

my_other_list.insert(1,"Azul")  # Insertar elemento en una posicion determinada
print(my_other_list) 
 
my_other_list.remove(1.70)      # eliminar elemento en especifico
print(my_other_list)

print(my_other_list.pop())      # eliminar elemento en un posicion determinado y saber que elemento es
print(my_other_list)
 
variable_pop = my_other_list.pop(1) # pop se utiliza comunmente para ir desasiendo la lista de desde el ultimo elemento
print(variable_pop)
print(my_other_list)
 
del my_other_list[0]            # eliminar sin mas elemento en una posicion
print(my_other_list)

my_new_list = my_other_list.copy()  # Copiar
my_other_list.clear()           # Vaciar lista
print(my_other_list)
print(my_new_list)

my_new_list.reverse()           # invertir lista
print(my_new_list)

print(my_list)
my_list.sort()                  # Ordenar
print(my_list)

print(my_list[1:3])             # sublista de elementos entre tal y tal posicion

