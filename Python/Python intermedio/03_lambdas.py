# lambdas

# lambdas son funciones anonimas

suma = lambda primer_valor, segundo_valor: primer_valor + segundo_valor

print(suma(2, 4))

multiplicacion = lambda uno, dos: uno * dos - 3
print(multiplicacion(2,4))

def suma_valores(valor_uno):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + valor_uno 

print(suma_valores(5)(2,4))
