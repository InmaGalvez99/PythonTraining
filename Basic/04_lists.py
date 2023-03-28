## Listas son mutables

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.56, "Inma", "Gálvez"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[4]) IndexError
print(my_other_list.count("Inma"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age , surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)


my_other_list.insert(1, "azul") #añade el elemento azul en el puesto 1
print(my_other_list)

my_other_list.append("inmion") #añade el elemento al final de la lista
print(my_other_list)

my_other_list.remove("azul") #elimina el elemento azul
print(my_other_list)

print(my_list.pop()) #quita el último elemento
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

print(my_list.pop(4)) #elimina el elemento 4
print(my_list)

my_new_list = my_list.copy()

my_list.clear() #elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #da la vuelta a la lista, ordena la lista al revés
print(my_new_list)

my_new_list.sort() #ordenar de menor a mayor
print(my_new_list)

print(my_new_list[1:2])

my_list = "hola python"
print(my_list)
