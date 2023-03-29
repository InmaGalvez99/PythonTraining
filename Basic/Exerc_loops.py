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