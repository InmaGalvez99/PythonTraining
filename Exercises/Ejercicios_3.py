"""
1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def maximo(a,b):
    if a > b:
        print(a)
    else:
        print(b)

maximo(10,15)


"""
2. Define una función máximo de 3 números y que devuelva el mayor. """

def max_funcion(a,b,c):
    if a > b > c:
        return a
    elif b > a > c:
        return b
    else:
        return c
    
max_funcion(-2,1,-7)



"""
3. Define una función que calcule la longitud de una lista, sin utilizar la función len()"""

def longitud(lista):
    contador = 0
    for i in lista:
        contador += 1
    return contador 
longitud("rinoplastia")


"""
4. Escribe una función que tome un carácter y devuelva True si es una vocal, de lo contrario que devuelva False"""

def vocales(caracter):
    if caracter in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False
vocales("h")


"""
5. Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""

## FUNCION SUMAR ##
def sumar(lista):
    resultado = 0
    for n in lista:
        resultado = resultado + n
    return resultado

lista = [1,5,3]
sumar(lista)

## FUNCION MULTIPLICAR ##

def multiplicacion (lista):
    resultado1 = 1
    for n in lista:
        resultado1 = resultado1 * n
    return resultado1
multiplicacion(lista)


"""
6. Calcule la funcion inversa de una cadena"""

def inversa(cadena):
    invertida = cadena[::-1]
    return invertida
inversa("hola mundo")


"""
7. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)"""

def palindromo(cadena):
    inicio = 0
    fin = len(cadena) -1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False
palindromo("radar")



"""
8. Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    for i in lista1:
        for n in lista2:
            if n in lista1:
                return True
            else:
                return False
lista1 = [1,2,4,5]
lista2 = [5,6]
superposicion(lista1,lista2)


"""
9. Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""

def generar_n_caracteres(num, x):
    total_caracteres = str("x") * num
    return total_caracteres
generar_n_caracteres(5, "x")