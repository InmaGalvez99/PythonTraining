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
    print("yo estudio" + subject)



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