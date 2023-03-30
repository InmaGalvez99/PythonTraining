### ERROR TYPES

# SyntaxError

#print"¡Hola comunidad!" # Error
print("¡Hola comunidad!")


# NameError

#print(age) # not defined
age = 23
print(age)


# IndexError
my_list= ["Python", "Swift", "Kotlin", "JavaScript"]
print(my_list[0])
print(my_list[-3])
#print(my_list[5]) # no hay elemento 5


# ModuleNotFoundError
#import maths
import math


#AttributeError
#print(math.PI) Error PI
print(math.pi)

# KeyErrora
my_dict = {"Nombre":"Inma", "Apellido":"Gálvez", "Edad": 23, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"])


# TypeError
#print(my_list["Nombre"]) la lista no permite str

#ImportError
#from math import PI 
from math import pi
print(pi)

#ValueError
#my_int= int("10 años")
my_int= int("10")
print(type(my_int))


#ZeroDivisionError
print(4/2)
#print(4/0)