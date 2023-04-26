"""
EJERCICIO 1: Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
"""
def my_function ():
    print("¡Hola amiga!")
    return
my_function()


"""
EJERCICO 2:Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el 
saludo ¡hola <nombre>!. """

def saludo(nombre):
    print("¡Hola " + nombre + "!")

saludo("Inma")
saludo("Antonio")


"""
EJERCICIO 3: Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def factorial(n):
    num = 1
    for i in range(n):
        num *= i+1
    return num

print(factorial(4))
print(factorial(20))


"""
EJERCICIO 4: Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la 
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

def factura(cantidad, iva=21):
    return cantidad + cantidad*iva/100
print(factura(100))
print(factura(2500))


"""
EJERCICIO 5: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un 
cilindro usando la primera función."""

def círculo_area (radio):
    pi = 3.1415
    return pi*radio**2

def cilindro_volume(radio,high):
    return círculo_area(radio)*high

print(cilindro_volume(5,8))



"""
EJERCICIO 6: Escribir una función que reciba una muestra de números en una lista y devuelva su media, 
varianza y desviación típica en un diccionario."""

def media (muestra):
    return sum(muestra)/len(muestra)

print(media([1,2,3,4,5]))
print(media([2.3,5.8,6.7,9.8,12.3,15.9]))


"""
EJERCICIO 7: Escribir una función que reciba una muestra de números en una lista y devuelva otra lista 
con sus cuadrados."""

def cuadrados(muestra):
    list = []
    for i in muestra:
        list.append(i**2)
    return list

print(cuadrados([1,2,3,4,5]))
print(cuadrados([2.3,5.8,6.7,9.8,12.3,15.9]))


"""
EJERCICIO 8: Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario 
con su media, varianza y desviación típica."""

def cuadrados(muestra):
    list = []
    for i in muestra:
        list.append(i**2)
    return list

def estadistica (muestra):
    stat = {}
    stat["Media"] = sum(muestra)/len(muestra)
    stat ["Varianza"] = sum(cuadrados(muestra))/len(muestra) - stat["Media"]**2
    stat["Desviación típica"] = stat["Varianza"]**0.5

print(estadistica([1,2,3,4,5]))
print(estadistica([2.3,5.8,6.7,9.8,12.3,15.9]))


"""
EJERCICIO 9: Escribir una función que calcule el máximo común divisor de dos números y otra que calcule 
el mínimo común múltiplo."""

def mcd (n, m):
    rest = 0
    while m > 0:
        rest = m
        m = n % m
        n = rest
    return n

def mcm (n, m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))


"""
EJERCICIO 10: Escribir una función que convierta un número decimal en binario y otra que convierta un 
número binario en decimal."""

def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) *2 ** i
    return decimal

def to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return "".join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))


"""
EJERCICIO 11: Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con 
la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i]= 1
    return words

def most_repeated(words):
    max_word= ""
    max_freq = 0
    for word,freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = "Como quieres que te quiera si el que quiero no me quiere como quiero que me quiera"
print(count_words(text))
print(most_repeated(count_words(text)))
