""" EJERCICIO 2: Escribir un programa que almacene la cadena ¡Hola Mundo! 
en una variable y luego muestre por pantalla el contenido de la variable """

Mensaje = "Hola mundo"
print(Mensaje)


""" EJERCICIO 3 : Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
donde <nombre> es el nombre que el usuario haya introducido"""

Nombre = input("Introduce su nombre: ")
print("¡Hola", Nombre, "!")



""" EJERCICIO 4: Escribir un programa que muestre por pantalla el resultado 
de la siguiente operación aritmética  (3+22⋅5 """

print (((3+2) / (2*5)) ** 2)



""" EJERCICIO 5: Escribe un programa que pregunte al usuario por el número de horas 
trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde"""

Horas = int (input("Introduce tus horas de trabajo: "))
Coste = float (input("Introduce lo que cobras por hora: "))
paga =  Horas * Coste

print( "Tu paga es", paga)



""" EJERCICIO 6: Escribir un programa que lea un entero porsitivo,  n , 
introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma 
suma=n(n+1)2 """

n = int (input("Introduce un número entero: "))
suma = n * (n+1)/2
print("La suma de los primeros número enteros desde 1 hasta", str(n),"es", str(suma))




""" EJERCICIO 7: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado 
con dos decimales"""

Peso = input("¿Cuál es tu peso en kg?: ")
Estatura = input("¿Cuál es su estatura en metros?: ")
IMC = round(float(Peso)/ float(Estatura) ** 2, 2)
print("Tu índice de masa corporal es", str(IMC))




""" EJERCICIO 8: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
 y <c> y <r> son el cociente y el resto de la división entera respectivamente"""

n = input("Introduzca el dividendo(entero): ")
m = input ("Introduzca el divisor (entero): ")
print(n, "entre", m, "da un cociente", str(int(n) // int(m)), "y un resto", str(int(n) % int(m)))




""" EJERCICIO 9: Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés porcentual anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión redondeado con dos decimales"""

cantidad = float(input("¿Cantidad a invertir? "))
interés = float(input("¿Tipo de interés? "))
años = int(input("¿Años? "))

print("Capital final:", str(round(cantidad * (interés/100 + 1) ** años, 2)))


""" EJERCICIO 10: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y 
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y 
calcule el peso total del paquete que será enviado """

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
precio_total= peso_payaso * payasos + peso_muñeca * muñecas

print("El peso total del paquete enviado es de", str(precio_total))


""" EJERCICIO 11: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la 
cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la 
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales"""

cantidad_depositada = input("Introduzca la cantidad depositada: ")
interés: 0.04
balance_1= cantidad_depositada * (interés + 1)
print ("El balance del primer año es", str(round(balance_1, 2)))
balance_2 = cantidad_depositada * (interés +2)
print ("El balance del segundo año es", str(round(balance_2, 2)))
balance_3= cantidad_depositada * (interés + 3)
print ("El balance del tercer año es", str(round(balance_3, 2)))



""" EJERCICIO 12: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un 
descuento del 60%. Escribe un programa que comience leyendo el número de barras vendidas que no son del día. 
Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por 
no ser fresca y el coste final total """

barras_no_frescas = int(input("Introduzca el número de barras de pan no frescas"))
descuento = 0.60
precio = 3.49
coste = barras_no_frescas * precio * (1 - descuento)

print("El precio de una barra es", str(precio), "€")
print ( "El descuento a una barra no fresca es", str(descuento * 100), "%")
print("El coste final a pagar es",str(round(coste, 2)), "€" )