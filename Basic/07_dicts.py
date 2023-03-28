## DICCIONARIOS

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_dict ={"Nombre":"Inma", "Apellido":"Gálvez", "Edad":23, 1:"python"}
my_other_dict = {
                "Nombre":"Inma", 
                 "Apellido": "Gálvez", 
                 "Edad":23, 
                 "lenguajes":{"python","sql", "pbi"},
                 1: 1.53
                 }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

my_dict ["Nombre"] = "Maria"
print(my_dict["Nombre"])

my_dict ["Calle"] ="Calle Rosa"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Gálvez" in my_dict) #false porque se busca por valor 
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys("Nombre", 1))

my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict)
