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


"""
EJERCICIO 3: Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos 
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70 

"""

frutas = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
fruta = input("Introduce el nombre de una fruta: ").capitalize()
kg = float(input("Número de kg: "))
if fruta in frutas:
    print(kg, "kilos de", fruta, "valen", frutas[fruta]*kg, "€")
else:
    print("Lo siento, la fruta ", fruta, "no la tenemos")


"""
EJERCICIO 4: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la 
misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

meses = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"septiembre", 10:"octubre", 11:"noviemnre", 12:"diciembre"}
fecha = input("Introduce una fecha en formato dd/mm/aaaa ")
fecha = fecha.split('/')
print(fecha[0], "de", meses[int(fecha[1])], "de", fecha[2])


"""
EJERCICIO 5: Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del 
curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

asignaturas = {"Matemáticass": 6, "Física":4, "Química":5}
total_créditos = 0
for asignatura, crédito in asignaturas.items():
    print(asignatura, "tiene", crédito, "créditos")
    total_créditos += crédito
print("número total de créditos de curso", total_créditos)



"""
EJERCICIO 6: Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre 
una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

persona = {}
continuar = True
while continuar:
    clave = input("¿Qué dato quieres añadir?")
    valor = input(clave + ": ")
    persona[clave] = valor
    print(persona)
    continuar = input("¿Quieres añadir más información (Si/No) ") == "Si"


