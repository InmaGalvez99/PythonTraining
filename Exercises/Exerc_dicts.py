"""
EJERCICIOS 1: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no 
está en el diccionario. """

monedas = {"Euro": "€", "Dollar":"$", "Yen": "¥"}
change= input("Que divisa quiere: ")
print(monedas.get(change.capitalize()), "La divisa no esta." )



"""
EJERCICIO 2: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>. """

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
dirección = input ("¿Dónde vives? ")
teléfono = input ("¿Cuál es tu número de teléfono? ")
persona = {"Nombre": nombre, "Edad": edad, "Dirección": dirección, "Teléfono": teléfono}
print(persona["Nombre"], "tiene", persona["Edad"], "años,", "vive en ", persona["Dirección"], "y su número de télefono es", persona["Teléfono"])


"""
EJERCICIO 3: Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos 
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70 

"""

frutas = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
fruta = input("Introduce el nombre de una fruta: ").capitalize()
kg = float(input("Número de kg: "))
if fruta in frutas:
    print(kg, "kilos de", fruta, "valen", frutas[fruta]*kg, "€")
else:
    print("Lo siento, la fruta ", fruta, "no la tenemos")


"""
EJERCICIO 4: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la 
misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

meses = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"septiembre", 10:"octubre", 11:"noviemnre", 12:"diciembre"}
fecha = input("Introduce una fecha en formato dd/mm/aaaa ")
fecha = fecha.split('/')
print(fecha[0], "de", meses[int(fecha[1])], "de", fecha[2])


"""
EJERCICIO 5: Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del 
curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

asignaturas = {"Matemáticass": 6, "Física":4, "Química":5}
total_créditos = 0
for asignatura, crédito in asignaturas.items():
    print(asignatura, "tiene", crédito, "créditos")
    total_créditos += crédito
print("número total de créditos de curso", total_créditos)



"""
EJERCICIO 6: Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre 
una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

persona = {}
continuar = True
while continuar:
    clave = input("¿Qué dato quieres añadir?")
    valor = input(clave + ": ")
    persona[clave] = valor
    print(persona)
    continuar = input("¿Quieres añadir más información (Si/No) ") == "Si"


"""
EJERCICIO 7: Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
...	...
Total	    Coste

"""

compra = {}
continuar = True
while continuar:
    artículo = input("Introduce un artículo: ")
    precio = float(input("Introduce el precio " + artículo + " :"))
    compra[artículo] = precio
    continuar = str.capitalize(input("¿Quieres añadir otro artículo? (Si/No): ")) == "Si"
coste = 0
print("Lista de la compra")
for artículo, precio in compra.items():
    print(artículo, "\t" , precio)
    coste += precio
print("Coste total ", coste)



"""
EJERCICIO 8: Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
 las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por 
 comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase 
 en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el 
 diccionario debe dejarla sin traducir."""

diccionario = {}
palabras = input("Introduce las palabras y su traducción con el formato palabra:traducción separado por comas: ")
for i in palabras.split(","):
    clave, valor = i.split(":")
    diccionario[palabras] = valor
frase = input("introduce una frase en español: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end= " ")
    else:
        print(i, end= " ")


"""
EJERCICIO 9: Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el 
valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar 
una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste 
y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se 
eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad 
cobrada hasta el momento y la cantidad pendiente de cobro. """

facturas = {}
cobrado = 0
pendiente = 0
more = " "
while more != "T":
    if more == "A":
        clave = input("Introduce el número de la factura: ")
        coste = float(input("Introduce el coste: "))
        facturas[clave] = coste
        pendiente += coste
    if more == "P":
        clave = input("Introduce el número de factura a pagar: ")
        coste = facturas.pop(clave,0)
        cobrado += coste
        pendiente -= coste
    print("Recaudado: ", cobrado)
    print("Pendiente de cobro: ", pendiente)
    more = input("¿Quieres añadir una nueva fatura (A), pagarla (P) o terminar (T)?: ")



"""
EJERCICIO 10: Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será 
otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos 
los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.  """

clientes = {}
opcion = " "
while opcion != "6":
    if opcion == "1":
        nif = input("Introduce el NIF del cliente: ")
        nombre= input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce la dirección del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        vip = input("¿Es un cliente preferente?: ")
        cliente ={"Nombre":nombre, "Dirección":direccion, "Teléfono":telefono, "Correo":correo, "Preferente":vip == "S"}
        clientes[nif] = cliente
    if opcion == "2":
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("No existe el cliente con el NIF ", nif)
    if opcion == "3":
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print("NIF: ", nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ":", valor)
        else:
            print("No existe el cliente con el NIF: ", nif)
    if opcion == "4":
        print("Lista de clientes")
        for clave, valor in clientes.items():
            print(clave,valor["Nombre"])
    if opcion == "5":
        print("Lista de clientes preferentes")
        for clave, valor in clientes.items():
            if valor["Preferente"]:
                print(clave, valor["Nombre"])
    opcion = input("Menú de opciones\n1 Añadir cliente\n2 Eliminar cliente\n3 Mostrar cliente\n4 Listar cliente\n5 Listar cliente preferente\n6 Terminar\n Elige una opción:")



"""
EJERCICIO 11: El directorio de los clientes de una empresa está organizado en una cadena de texto como la de 
más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se 
le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.
"nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento 
corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información 
del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. 
Es decir, un diccionario como el siguiente
{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}

"""
# cadena de datos del cliente
datos_cliente = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
lista_clientes = datos_cliente.split("\n")
directorio ={}
lista_campos = lista_clientes[0].split(";")
for i in lista_clientes[1:]:
    cliente = {}
    lista_info= i.split(";")
    for j in range(len(lista_campos)):
        if lista_campos[j] == "descuento":
            lista_info[j] = float(lista_info[j])
            cliente[lista_campos[j]] = lista_info[j]
    directorio[lista_info[0]] = cliente
print(directorio)