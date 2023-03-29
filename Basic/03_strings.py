## strings ##

my_string = "mi string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\teste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\teste es un string \n escapado"
print(my_scape_string)

my_scape_string = "\teste es un string \n escapado"
print(my_scape_string)

## formateo

name, surname, age = "Inma", "Gálvez", 23
print("mi nombre es {} {} y mi edad es {}". format(name,surname,age))
print("mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"mi nombre es {name} {surname} y mi edad es {age}")

""" %.2f devuelve un númeor decimal redondeado a dos decimales
%f devuele un número decimal 
%d ignora los decimales """


# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(d)

# división

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [0:6:2]
print(language_slice)


#reverse

reversed_language = language [::-1]
print (reversed_language)

# Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))