 # Variables

my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_str_variables = str(my_int_variable)
print(my_int_str_variables)
print(type(my_int_str_variables))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de :", my_bool_variable)

# Algunas funciones del sistema
print(len(my_variable))

# Variables en una sola línea. ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Inma", "Gálvez", "Inmi", 23
print("Me llamo :", name,surname, "mi edad es:", age, "y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuantos años tienes? ')

print(name)
print(age)