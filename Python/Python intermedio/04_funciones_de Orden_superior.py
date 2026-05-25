# Funciones de orden superior

def suma_uno(valor_uno):
    return valor_uno + 1

def suma_cinco(valor_uno):
    return valor_uno + 5


def suma_valores(uno,dos,funcion):
    return funcion(uno + dos)

print(suma_valores(5,2,suma_uno))
print(suma_valores(5,2,suma_cinco))

# closures funcion que retorna funcion

def suma_10():
    def add(valor):
        return valor + 10
    return add

add_closere = suma_10()

print(add_closere(5))

# Funciones de orden superior que existen en el sist

numers = [2,5,10,21,3,30]

# map: recorre todos los valores y ejecuta una funcion sobre ellos para modificar su valor
def x_2 (numero):
    return numero * 2

print(list(map(x_2, numers)))
print(list(map(lambda number: number * 2, numers)))

# filter: recorre todos los valores y ejecuta una funcion de retorna true o false para saber com filtrar los valores del iterable

def filtro(number):
    if number > 10:
        return True
    return False
           
print(list(filter(filtro, numers)))
print(list(filter(lambda number: number > 10, numers)))




