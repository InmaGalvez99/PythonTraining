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



"""
EJERCICIO 6: Escribir una función reciba una lista de notas y devuelva la lista de calificaciones 
correspondientes a esas notas."""

def calificación (score):
    if score < 5:
        return 'S'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'
    
def aplica_calificación (scores):
    return list(map(calificación, scores))

print (aplica_calificación([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))



"""
EJERCICIO 7: Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas."""

def grade (score):
    if score < 5:
        return 'S'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'
    
def apply_grade (scores):
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects,grades))

print(apply_grade({'Matemáticas': 8.0, 'Inglés': 9.5, 'Química': 3.45, 'Lengua': 10, 'Naturales': 2.75}))



"""
EJERCICIO 8: Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas 
aprobadas."""

def grade(score):
    if score < 5:
        return 'S'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'
     
def passed_subjects(subject):
    return (subject[1] >= 5)

def apply_grade(scores):
    passed = dict(filter(passed_subjects, scores.items()))
    grades = map(grade, passed.values())
    subjects = map(str.upper, passed.keys())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas': 8.0, 'Inglés': 9.5, 'Química': 3.45, 'Lengua': 10, 'Naturales': 2.75}))



"""
EJERCICIO 9: Escribir una función que calcule el módulo de un vector."""

def square(x, y):
    return x+ y **2

def module (v):
    from functools import reduce
    return reduce(square, v, 0) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))


"""
EJERCICIO 10: Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles 
cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un 
nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las 
siguiente fórmula en función de la zona:

Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5"""

pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio =(piso['metros'] *100 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_pisos(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro, map(añadir_precio,pisos)))

print(busca_pisos(pisos,100000))


"""
EJERCICIO 11: Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, 
los valores cuya puntuación típica sea mayor que 3 o menor que -3.
Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de 
la muestra."""

from statistics import mean, stdev

def típica (muestra):
    media = mean(muestra)
    desviación = stdev(muestra)
    def f(n):
        puntuación = (n - media) / desviación
        return (puntuación < -3) or (puntuación > 3)
    return f

def puntuación_típica (muestra):
    return list(filter(típica(muestra), muestra))

print(puntuación_típica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
