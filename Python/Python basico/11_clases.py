# Clases

class Persona:                          # los nombres de las clases se declaran con mayusculas y sin espacios
    def __init__(self,name,surname):    # construcor de clase sirve para inicializar
        self.name = name
        self.__surname = surname        # con dos giones bajos (__) puedo hacer el cinstructor privado
    
    def get_surname(self):
        return self.__surname
    
    def Wolk (self):                    # puedo definir funciones dentro de una clase
        print(f"{self.name} esta caminado")
       
my_person = Persona("Kevin","Sosa")
print(my_person)
print(my_person.name)

my_person.Wolk()
print(my_person.get_surname())





