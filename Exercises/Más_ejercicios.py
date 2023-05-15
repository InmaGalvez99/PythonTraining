"""
1. Escribir un programa que lea un numero par por teclado. Si el usuario introduce un numero impar, debe repetirse el proceso hasta que lo introduzca correctamente."""

while True:
    numero= int(input("introduce un numero par: "))
    if numero % 2 != 0:
        print("Este número es impar, introduce un número par")
    else:
        print("El número es par, final")
        break



"""
2. Escribir un programa que pida el usuario cuantos numeros quiere introducir. Luego, que lea todos los numeros y realice una media aritmetica """

num = int(input("introduce una cantidad de números: "))
numeros = []
for i in range(num):
    m = float(input("introduce el número {}: ".format(i + 1)))
    numeros.append(m)

print("La media de los numeros es ", sum(numeros)/len(numeros))


"""
3. Utilizando la función range() y la conversión a listas, generar las siguientes listas dinámicamente:
Todos los números pares del 0 al 20
Todos los números múltiplos de 5 del 0 al 50
"""

print([x for x in range(0, 21) if x%2 == 0]) ## lista de pares
print([x for x in range(0,51) if x%5 == 0]) ## lista de múltiplos


