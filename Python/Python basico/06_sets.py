# Sets

my_sets = set()
my_other_sets = {}          # los sets y diccionarios se definen igual

print(type(my_sets))
print(type(my_other_sets))  # inicialmente es un diccionario

my_other_sets = {'Kevin','Sosa',22}

print(type(my_other_sets))  # al darle valores se convierte en set
 
print(len(my_other_sets))
print(my_other_sets)        

my_other_sets.add("Viejoke")
print(my_other_sets)        # un set no es una estructura ordenada

my_other_sets.add("Viejoke")
print(my_other_sets)        # un set no admite repetidos

print("Sosa" in my_other_sets)
print("soso" in my_other_sets)

my_other_sets.remove(22)
print(my_other_sets)

my_other_sets.clear()
print(len(my_other_sets))

my_sets =  {'Kevin','Sosa',22}
my_list = list(my_sets)
print(my_list)
print(my_list[0])

my_other_sets = {'C','C++','Python'}

my_new_set = my_sets.union(my_other_sets)
print(my_new_set)
 
