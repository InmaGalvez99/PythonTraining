""" EJERCICIO 1: Escribir un programa que pregunte el nombre del usuario en la consola y 
un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces 
como el número introducido """

nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre, "/n"), int(n))



""" EJERCICIO 2: Escribir un programa que pregunte el nombre completo del usuario en la consola y 
después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en 
mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera """

nombre = input ("¿Cuál es tu nombre completo? ")
print (nombre.lower())
print(nombre.upper())
print (nombre.title())




""" EJERCICIO 3: Escribir un programa que pregunte el nombre del usuario en la consola y después 
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el 
nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre """

nombre = input ("¿Cómo te llamas?")
print(nombre.upper(),"tiene", str(len(nombre)),  "letras")




""" EJERCICIO 4: Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde 
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por 
pantalla el número de teléfono sin el prefijo y la extensión """

teléfono = input("Introduce el número de tlf con el formato -xx-xxxxxxxxx-xx: ")
print("El número del tlf es", teléfono[4:-3])




""" EJERCICIO 5: Escribir un programa que pida al usuario que introduzca una frase en la consola y 
muestre por pantalla la frase invertida """

frase =input("introduce una frase: ")
print(frase[::-1])




""" EJERCICIO 6: Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal 
en minúscula, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula"""

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula: ")
print(frase.replace(vocal, vocal.upper()))




""" EJERCICIO 7: Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre 
por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
dominio ceu.es """

correo_electrónico = input("introduce su correo electrónico: ")
print(correo_electrónico[:correo_electrónico.find("@")]+"@ceu.es")




""" EJERCICIO 8: Escribir un programa que pregunte por consola el precio de un producto en euros con dos 
decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido """


precio = input("introduce el precio del produco con dos decimales: ")
print(precio[:precio.find(".")], "euros y", precio[precio.find(".") +1:], "céntimos")



""" EJERCICIO 9: Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año"""

fecha = input ("introduce la fecha de su nacimiento en formato dd/mm/aaaa: ")
print("Día", fecha[:2])
print("Mes", fecha[3:5])
print ("Año", fecha[-4:])




""" EJERCICIO 10: Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta """

productos_compra = input("Introduce los productos de la compra separados por comas: ")
print (productos_compra.replace(",", "\n"))




""" EJERCICIO 11: Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
 y muestre por pantalla una cadena con el siguiente formato:

<producto>: <unidades> unidades x <precio>€ = <total>€

donde <unidades> es el número de unidades con cinco dígitos, <precio> es el precio unitario con 6 dígitos 
enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2 decimales"""

producto = input ("Introduce el nombre del producto: ")
precio = float (input("Introduce el precio del producto: "))
unidades = int (input("Introduce el número de unidades del producto: "))
print ("{producto}:, {unidades} unidades * {precio}€ = {total}€".format(producto=producto, precio=precio, unidades=unidades, total=unidades*precio))