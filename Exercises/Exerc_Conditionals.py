"""EJERCICIO 1: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no"""


edad = int(input("¿Cuál es tu edad?: "))
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")



""" EJERCICIO 2: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas"""

 
my_variable = "contraseña"
my_password = input("Introduce la contraseña: ")

if my_variable == my_password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")



""" EJERCICIO 3: Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario 
no introduce números debe devolver un aviso de error y si el divisor es cero también """

n = float(input("Introduce el dividendo: "))
m = float (input("Introduce el divisor: "))
if m == 0:
    print("Error. No se puede dividir entre 0")
else:
    print(n/m)




""" EJERCICIO 4: Escribir un programa que pida al usuario un número entero y muestre por pantalla 
si es par o impar."""

n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")



"""EJERCICIO 5: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar o no."""

age = int(input("¿Cuál es tu edad?: "))
income = float(input("¿Cuáles son tus ingresos mensuales?: "))

if age > 16 and income >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")



"""EJERCICIO 6: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a 
la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde."""

name = input ("¿Cómo te llamas?: ")
gender = input ("¿Cuál es tu sexo (F o M)?: ")

if gender == "F":
    if name < "M":
       group = "A"
    else:
        group = "B"

if gender =="M":
    if name > "N":
        group = "A"
    else:
        group = "B"

print ("Tu grupo es" + group)


# Otra forma

name = input ("¿Cómo te llamas?: ")
gender = input ("¿Cuál es tu sexo (F o M)?: ")

if ((gender == "F" and name < "M") or gender == "H" and name > "N"):
    group = "A"
else:
    group = "B"

print("Tu grupo es "+ group)



"""
EJERCICIO 7: Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	           Tipo impositivo
Menos de 10000€	        5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar. """

renta =float(input("¿Cuál es su renta anual?: "))

if renta < 10000:
    tipo = 5
elif renta < 20000:
    tip = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

print("Tienes que pagar", renta * tipo / 100, "€")




"""
EJERCICIO 8: En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en 
mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4. o 0.6,pero no valores 
intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes 
a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la 
cantidad de dinero que recibirá el usuario """

bonificación = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6

puntos = float(input("Introduce su puntación: "))
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = " "

if nivel == " ":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel) # también puedes poner {}.format(nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificación))  # devuelve un número decimal con dos decimales



"""
EJERCICIO 9: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere 
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar 
al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar
gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. 
"""

age = int(input("Introduce su edad: "))

if age < 4:
    entrada = "gratis"
elif age > 4 and age < 18:
    entrada = 5
else:
    entrada = 10

print("El precio de la entrada es", entrada, "€")


"""
EJERCICIO 10: La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un 
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por 
pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("Bienvenido a la pizzería Bella Napoli. \nTipos de pizza: \n\t1 Pizza vegetariana \n\t2 Pizza no vegetariana")
tipo= input("Elige el número correspondiente al tipo de pizza que desee: ")

if tipo == "1":
    print("Ingredientes de pizzas vegetarianas: \n\t1 Pimineto \n\t2 Tofu")
    ingrediente= input("Introduce el ingrediente que quiera: ")
    print("Pizza vegetariana con mozarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingrediente de pizzas no vegerarianas: \n\t1 Peperoni \n\t2 Jamón \n\t3 Salmón")
    ingrediente= input("Introduce el ingrediente que quiera: ")
    print("Pizza no vegetariana con mozarella, tomate y ", end="")
    if ingrediente =="1":
        print("peperoni")
    elif ingrediente =="2":
        print("jamón")
    else:
        print("salmón")