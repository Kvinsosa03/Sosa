# funciones

def my_function():
    print("Esto es un funcion")
    
my_function()
     
def suma_dos_numeros(a,b):
    print(a+b)
    
suma_dos_numeros(5,7)

def suma_dos_numeros_retornar(a,b):
    return a+b
    
my_resultado = suma_dos_numeros_retornar(8,7) 

print(my_resultado)

def print_name(name,surname):
    print(f"{name} {surname}")
    
print_name("Kevin","Sosa")

def print_name(name,surname):
    print(name,surname)
    
print_name("Kevin","Sosa")

def print_name_con_defeault(name,surname,age=22):
    print(f"{name} {surname} {age}")
    
print_name_con_defeault("Kevin","Sosa",)

def print_text(*text):
    for text in text:
        print(text.upper())
    
print_text("Hola","Kevin","Sosa",)

    