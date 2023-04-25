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