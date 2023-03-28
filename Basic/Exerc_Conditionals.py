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