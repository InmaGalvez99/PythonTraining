"""EJERCICIO 1: Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla si es mayor de edad o no"""


print("¿Cuál es tu edad?")
my_condition = 18

if my_condition < 18:
    print("Soy mayor de edad")
else:
    print("Soy menor de edad")



""" EJERCICIO 2: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
##pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
##por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas"""

 #CORREGIR
 
"""my_variable = "contraseña"
my_password = "contraseña"
print ("Introduce la contraseña ")

if my_variable == my_password:
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")"""


key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")