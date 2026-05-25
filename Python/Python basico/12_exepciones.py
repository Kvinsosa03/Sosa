# exepciones

numero_uno = 5
numero_dos = "3"

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error") 
else:   # ocional
    # se ejecuta si no se produce error
    print("La ejecucion continua correctamente")
finally:    #opcional
    # se ejecuta siempre        
    print("La ejecucion continua")    
    
numero_uno = 5
numero_dos = 3

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error") 
else:
    # se ejecuta si no se produce error
    print("La ejecucion continua correctamente")
finally:        
    print("La ejecucion continua")  
    
# si queremos captar un tipo de error especifico

numero_uno = 5
numero_dos = "3"

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")     
except TypeError:
    print("Se ha producido un typeError") 

# guardar el error
  
numero_uno = 5
numero_dos = "3"

try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")    
except TypeError as error:
    print(error)   
    
    
