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


"""
4. Dadas dos listas(las que se quiera crear), generar una tercera con los elementos que estén presentes en AMBAS listas."""

list1= [1,2,3,4,5,6,7,8,9]
list2= [6,2,4,1,3]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)

print(list3)


"""
5. Escribir un programa que sume todos los números enteros impares desde 0 hasta 100 """

lista = []
for i in range(0,101):
    if i %2 != 0:
        lista.append(i)

print(sum(lista))


"""
6. Cuenta las veces que aparece un elemento en una lista."""

lista = [5,2,1,6,1,9,9,1,3,1]

print(lista.count(1))
