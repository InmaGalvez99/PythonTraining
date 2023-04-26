"""
EJERCICIO 1: Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la 
compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el 
IVA a los productos de la cesta y devolver el precio final de la cesta."""

def descuento(price, discount):
    return price - price*discount/100

def iva(price, porcentage):
    return price + price*porcentage / 100

def cesta(cesta, function):
    total = 0
    for price, discount in cesta.items():
        total += function(price,discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', cesta({1000:20, 500:10, 100:1}, descuento))
print('El precio de la compra tras aplicar el IVA es: ', cesta({1000:20, 500:10, 100:1}, iva))


"""
EJERCICIO 2: Escribir una función que simule una calculadora científica que permita calcular el seno, coseno,
tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar,
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la 
función a esos enteros."""

from math import sin, cos, tan, exp, log

def function(f, n):
    functions = {"sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log}
    result = {}
    for i in range(1, n+1):
        result[i]= functions[f](i)
    return result

def calculator():
    f = input("introduce la función a aplicar: (sin, cos, tan, exp, log)")
    n = int(input("Introduce un entero positivo"))
    for i, j in function(f,n).items():
        print( i, "\t", j)
    return
calculator()


"""
EJERCICIO 3: Escribir una función que reciba otra función y una lista, y devuelva otra lista con el 
resultado de aplicar la función dada a cada uno de los elementos de la lista."""

def function_list(funcion, lista):
    m = []
    for i in lista:
        m.append(funcion(i))
    return m 

def cuadrado(n):
    return n*n

print(function_list(cuadrado, [1,2,3,4]))


"""
EJERCICIO 4: Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista 
con los elementos de la lista que devuelvan True al aplicarles la función booleana."""

def funcion(funcion,lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(funcion(par, [1,2,3,4,5,6]))


"""
EJERCICIO 5: Escribir una función que reciba una frase y devuelva un diccionario con las palabras que 
contiene y su longitud."""

def palabras(frase):
    words = frase.split()
    lenght = map(len, words)
    return dict(zip(words, lenght))

print(palabras("Welcome to Python"))
