##LOOPS / BUCLE

# While  atado a cumplir una condición

my_condition = 0
while my_condition < 10: 
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("mi condición es mayor o igual que 10")

print ("la ejecución continúa")

while my_condition <20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break    #se detiene/rompe el bucle
    print(my_condition)

print ("la ejecución continúa")


## FOR ## atado a nº finito de datos. Itera estructuras que son iterables

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)


my_tuple = (23, 1.56, "Inma", "Gálvez", "inmion")

for element in my_tuple:
    print(element)

my_other_set = {"Inma", "Gálvez", 23}

for element in my_other_set:
    print(element)

my_dict ={"Nombre":"Inma", "Apellido":"Gálvez", "Edad":23, 1:"python"} 

for element in (my_dict):  # imprime las claves
    print(element)
    if element =="Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")


for element in (my_dict):  # imprime las claves
    print(element)
    if element =="Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")