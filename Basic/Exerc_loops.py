"""
EJERCICIO 1: Escribir un programa que pida al usuario una palabra y la muestre 10 veces por pantalla."""

word = input("Introduce una palabra: ")

for element in range(10):
    print(word)

"""
EJERCICIO 2: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
ha cumplido (desde 1 hasta su edad). """

age = int(input("Introduce su edad: "))

for element in range(age):
    print("Has cumplido", str(age +1), "años")


"""
EJERCICIO 3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas. """

number = int(input("Introduce un número entero positivo: "))
for i in range(1, number+1, 2 ):
    print(i, end= "," )

## lo mismo pero imprime todos los pares

number = int(input("Introduce un número entero positivo: "))
for i in range(1, number+1):
    if i % 2 == 0:
        print(i, end= ",")

"""
EJERCICIO 4: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas. """

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end= ",")



""" 
EJERCICIO 5: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
amount = float(input("Introduce la cantidad a invertir: "))
interest = float(input("Introduce el tipo de interés anual: "))
years = int(input("¿AÑos? "))

for i in range(years):
    amount *= 1 + interest/100
    print("Capital tras ", str(1+i), "años", str(round(amount, 2)))



"""
EJERCICIO 6: Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido. 

*
**
***
****
*****

"""

n = int(input("Introduce un número entero: "))
for i in range (n):
    print("*" * (i+1))

# otra forma
n = int(input("Introduce un número entero: "))
for i in range (n):
    for j in range(i+1):
        print("*", end="")
    print(" ")



"""
EJERCICIO 7: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. """

for i in range (1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print(" ")


"""
EJERCICIO 8: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido. 

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

n = int(input("Introduce un número entero: "))
for i in range (1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")


"""
EJERCICIO 9: Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. """

key = "contraseña"
password = ""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")