"""
EJERCICIO 1: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla. """

my_subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(my_subjects)



"""
EJERCICIO 2: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista. """

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("yo estudio " + subject)



"""
EJERCICIO 3: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es 
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el 
usuario. """

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores=[]
for subject in subjects:
    score = input("¿Que nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " he sacado " + scores[i])



"""
EJERCICIO 4: Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. """

lottery = []
for i in range(6):
    lottery.append(int(input("Introduce un número ganador: ")))
lottery.sor()
print("Los números ganadores son " + str(lottery))



"""
EJERCICIO 5: Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
pantalla en oren inverso separados por comas. """

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers)

# sin corchetes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end= ", ")


"""
EJERCICIO 6: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y 
elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas 
que el usuario tiene que repetir. """

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("Que nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))



"""
EJERCICIO 7: Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. """

alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
for  i in range(len(alphabet), 0, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)



"""
EJERCICIO 8: Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """

word = input("introduce una palabra: ")
reverse_word = word
word = list(word)
reverse_word = list(reverse_word)
reverse_word.reverse()

if word == reverse_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")



"""
EJERCICIO 9: Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces 
que contiene cada vocal. """

word = input("Introduce una palabra: ")
vocals = ["a", "e", "i", "o", "u"]

for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("la vocal " + vocal + "aparece " + str(times) + " veces" )



"""
EJERCICIO 10: Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 
8, y muestre por pantalla el menor y el mayor de los precios. """

prices = [50, 75, 46, 22, 80, 65, 8]
max = min = prices[0]  #posición cero
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El precio mínimo es " + str(min))
print ("El precio máximo es " + str(max))



"""
EJERCICIO 11: Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por 
pantalla su producto escalar. """

a = (1, 2, 3)
b = (-1, 0, 2)
resultado = 0
for i in range(len(a)):
    resultado += a[i] * b[i]
print("El producto de los vectores " + str(a) + " y" + str(b) + " es " + str(resultado))



"""
EJERCICIO 12: Escribir un programa que almacene las matrices
 
A = [1,2,3] y B= [-1,0]
    [4,5,6]      [0, 1]
                 [1, 1]

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una 
lista. """

 # 2x3  3x2 obtendremos una matriz 2x2

A = ((1, 2, 3),
     (4, 5, 6))

B = ((-1, 0),
     (0, 1),
     (1, 1,))

result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for t in range(len(result)):
    result[t]= tuple(result[t])
    print(result[t])

