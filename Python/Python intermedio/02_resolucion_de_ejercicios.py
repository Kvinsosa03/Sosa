# retos

'''
El famoso "FIZZ BUZZ"
escribe un programa que muesstre por consola(con un print)los 
numeros del 1 al 100(ambos incluidos y con un salto de linea entre
cada imprecion),sustituyendo los siguientes:
- multiplos de 3 por la palabra "fizz"
- multiplos de 5 por la palabra "buzz"
- multiplos de 3 y 5 por la palabra "fizzbuzz"

'''

def Fizzbuzz():
    for i in range(1,101):
        if i%5== 0 and i%3 == 0:
            print("fizzbuzz")
        elif i%3== 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
    
Fizzbuzz()

'''
Es un anagrama
Escribe una funcion que reciba dos palabras (String) y retorne 
verdadero o falso (bool) sugun sean o no anagramas.
- un anagrama consiste en formar una palabre reorddenando todas 
las letras de otra palabra inicial
- no hace falta comprobar que ambas palabras existan
- dos palabras exactamente iguales no son anagramas
'''

def anagrama(uno,dos):
    if uno == dos:      # comprobando si las palabras son iguales 
        return False
    return sorted(uno) == sorted(dos) # sorted ordena los caracteres

print(anagrama("amor","mora"))

'''
Sucesion de Fibonacci
Escribe un programa que imprima los 50 primeros numeros de la sucion 
de fibonacci empezando por 0
- fibonacci es la sisecion de numeros en la que la siguiente es la suma
 de los dos anteriores
'''

def fibonacci():
    previo = 0
    siguiente = 1
    for i in range(0,50):
        print(previo)
        suma = previo + siguiente
        previo = siguiente
        siguiente = suma
        
fibonacci()

'''
Es un numero primo
Escribe un programa que se encargue de comprobar si un numero es primo o no.
hecho esto, imprime los numeros primos del 1 al 100.
'''

def primo(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
               
                
for i in range(1,101):
    if primo(i) == True:
        print(i)
    
