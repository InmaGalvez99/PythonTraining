## CONDITIONALS

my_condition = False

if my_condition:
    print ("se ejecuta le condición del if")

print ("la ejecución continúa")


my_condition = 5 * 5

if my_condition == 10 :
    print ("se ejecuta le condición del segundo if")

print ("la ejecución continúa")

if my_condition > 10 :  
    print ("es mayor que 10")
else:
    print ("es menor o igual que 10")
    
print ("la ejecución continúa")


if my_condition > 10 and my_condition < 20: 
    print ("es mayor que 10 y menor que 20")
else:
    print ("es menor o igual que 10 o mayor o igual que 20")
    
print ("la ejecución continúa")


#orden de jerarquía: 1º if, 2º elif, 3º else
if my_condition == 10: 
    print("se ejecuta la confición cuarta del if")
if my_condition > 10 and my_condition < 20: 
    print ("es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("es igual a 25")
else:
    print ("es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
    
print ("la ejecución continúa")

my_string= ""

if not my_string: 
    print("mi cadena de texto es vacía")

if my_string == "mi cadena de textooooooo":
    print("estas cadenas de texto coinciden")