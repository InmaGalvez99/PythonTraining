## EXCEPTIONS  HANDLING ##

numberOne = 5
numberTwo = 1
numberTwo = "1"
 
# try except juntos siempre
try:
    print (numberOne + numberTwo)
    print("No se ha producido error")
except:
    # se ejecuta si se produce una excepción
    print ("Se ha producido un error")


# try except else finally

try:
    print (numberOne + numberTwo)
    print("No se ha producido error")
except:
    print ("Se ha producido un error")
else: # opcional
    # se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # opcional
    # se ejecuta simepre 
    print("La ejecución continúa")



# Excepciones por tipo

try:
    print (numberOne + numberTwo)
    print("No se ha producido error")
except ValueError:  # tipo de argumento correcto pero valor incorrecto  
    print ("Se ha producido un ValueErros")
except TypeError: # el tipo de dato del objetivo es inapropiado
    print ("Se ha producido un TypeError")


# captura de la información de la excepción

try:
    print (numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:    
    print (error)
except Exception as error: # objeto que representa un error
    print(error)