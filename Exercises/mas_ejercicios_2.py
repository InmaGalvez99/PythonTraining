"""
1. Crear tres variables nombradas f, g y h con valores numéricos cualesquiera; una cuarta llamada resultado que sea la suma de las primeras tres, y por último imprimir en pantalla el resultado.
"""

f = 10
g = 25
h = 3
resultado = f + g + h

print(f"El resultado de la suma {f} más {g} más {h} es {resultado}" )


"""
2. Crear dos variables, saludo y nombre, cuyos contenidos sean "Hola, " en el primer caso y tu nombre en el segundo solicitado mediante un "input". Intenta sumarlas vía el operador + y mostrar el resultado en pantalla. Para guardar el resultado de la suma puedes crear una tercera variable."""

saludo = "Hola, "
nombre = input("Introduce tu nombre: ")
bienvenida = saludo + nombre
print(bienvenida)


"""
3. Escriba un programa en Python que simule el resultado de colocar determinada cantidad de dinero en un plazo fijo. Para ello se deberán crear una serie de variables que se pedirán al usuario:

Capital

Tiempo en días

La tasa de interés es del 85% anual. Luego que el programa pide al usuario el tiempo que colocara el capital y el capital , calcule e imprima el interés que obtendrá producto de la operación."""

tasa = 0.85
capital= float(input("Introduce el capital deseado: "))
tiempo = int(input("Introduce los días: "))
interés = round(capital*tiempo*tasa/365, 2)

print(f"El interés es {interés} ")


"""
4. Paula hizo 3 exámenes, su nota final es el promedio de las 3 notas idividuales. Se desea saber su nota final sabiendo que:

nota1 = 6

nota2 = 8

nota3 = 5 """

nota1 = 6
nota2= 8
nota3 = 5
nota_final= round((nota1 + nota2 + nota3)/3, 2)
print(f"La nota final de Paula es {nota_final}")


"""
5. Elaborar un programa que reciba como input el signo del zodiaco de una persona y que devuelva como salida el tipo de elemento que corresponde a ese signo.

Signos de Fuego: Aries, Leo y Sagitario. Signos de Tierra: Tauro, Virgo y Capricornio. Signos de Aire: Géminis, Libra y Acuario. Signos de Agua: Cáncer, Escorpio y Piscis."""

signo = input("Introduce tu signo del zodíaco: ")
if signo == "aries" or signo == "leo" or signo == "sagitario":
    print("¡Tu signo es fuego!")
elif signo == "tauro" or signo == "virgo" or signo == "capricornio":
    print("¡Tu signo es tierra!")
elif signo == "géminis" or signo =="libra" or signo == "acuario":
    print("¡Tu signo es aire!")
elif signo == "piscis" or signo == "cáncer" or signo =="escorpio":
    print("¡Tu signo es agua!")
else:
    print("Error")


"""
6. Supongamos que una aerolínea tiene las siguientes tarifas de billetes para "niños": los niños de 2 años o menos vuelan gratis, los niños mayores de 2 pero menores de 13 pagan una tarifa de niño con descuento y cualquier persona de 13 años o más paga una tarifa de adulto normal. Elaborar un programa que reciba como input la edad y que devuelva como salida el tipo de tarifa."""

edad_tarifa = int(input("Introduce tu edad: "))
if edad_tarifa <= 2:
    print("tarifa niño")
elif edad_tarifa > 2 and edad_tarifa < 13:
    print ("tarifa niño con desucento")
else:
    print("tarifa adulto")


"""
7. Necesitamos clasificar los clientes de un negocio en funcion a sus ingresos:

Clasificacion de los ingresos:

● ingreso bajo: < 100000

● ingreso promedio: >= 100000 y menor a 500000

● ingreso alto: >500000

Elaborar un programa que reciba como input el ingreso del cliente y que devuelva como salida el tipo ingreso segun su clasificacion."""

ingreso_cliente = int(input("introduce tu ingreso: "))

if ingreso_cliente < 100000:
    print("tu ingreso es bajo")
elif ingreso_cliente >=100000 and ingreso_cliente < 500000:
    print("tu ingreso es promedio")
else:
    print("tu ingreso es alto")


"""
8. Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese un nombre. Luego, saludar al usuario."""

nombre = input("introduce tu nombre: ")
while nombre == "":
    print("Dato vacío")
    nombre = input("introduce tu nombre otra vez: ")

print("Hola " + nombre.capitalize())


"""
9. Dada una lista de números encontrar el promedio de sus elementos:

1 - Sin usar ninguna función.

2 - Usando funciones incorporadas de Python."""

## opcion 1 ##
numeros = [2,3,6,1,1,8,9,1,2,2,5,7,8,4]
suma = 0
num = 0
for i in numeros:
    suma += i
    num += 1
print(round(suma/num, 2))

## opcion 2 ##

print(round(sum(numeros)/len(numeros), 2))