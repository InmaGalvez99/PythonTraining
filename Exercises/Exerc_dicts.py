"""
EJERCICIOS 1: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no 
está en el diccionario. """

monedas = {"Euro": "€", "Dollar":"$", "Yen": "¥"}
change= input("Que divisa quiere: ")
print(monedas.get(change.capitalize()), "La divisa no esta." )



"""
EJERCICIO 2: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>. """

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
dirección = input ("¿Dónde vives? ")
teléfono = input ("¿Cuál es tu número de teléfono? ")
persona = {"Nombre": nombre, "Edad": edad, "Dirección": dirección, "Teléfono": teléfono}
print(persona["Nombre"], "tiene", persona["Edad"], "años,", "vive en ", persona["Dirección"], "y su número de télefono es", persona["Teléfono"])