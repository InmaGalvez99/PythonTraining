## SETS

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {"Inma", "Gálvez", 23}
print(type(my_other_set))

print(len(my_other_set))

print(my_other_set)

my_other_set.add("inmion") # un set no admite repetidos
print(my_other_set) # un set no es una estructura ordenada

print("Gálvez" in my_other_set)
print("Galve" in my_other_set)

my_other_set.remove("Gálvez")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#Print(my_other_set) NameError: name 'Print' is not defined

my_set =  {"Inma", "Gálvez", 23}
my_list = list(my_set) #este tipo de transformaciones no suele ser lo mejor
print(my_list)
print(my_list[0])

my_other_set =  {"sql", "pbi", "python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"}))

print(my_new_set.difference(my_set))

