# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Kevin","Apellido":"Sosa","Edad":22, 1:"Python"}
my_dict = {
    "Nombre":"Kevin",
    "Apellido":"Sosa",
    "Edad":22,
    "Lenguaje":{"C","C++","Java"},
    1 : 1.70
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict["Lenguaje"])

my_dict["Nombre"] = "Yaque"
print(my_dict["Nombre"])

my_dict["Escuela"] = "Cujae"
print(my_dict)

del my_dict["Escuela"]
print(my_dict)

print("Sosa" in my_dict)
print("Edad" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre","Edad","Piso"))   # crear un diccionario con claves sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)   
print(my_new_dict)

