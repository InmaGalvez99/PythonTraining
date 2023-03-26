## FUNCTIONS ##

def my_function ():
    print("Estos es una función")

my_function ()

def sum_two_values (first_number, second_number):
    print (first_number + second_number)

sum_two_values(5, 7)
sum_two_values (54919, 785)
sum_two_values("5", "7") #se convierte en cadenas de texto por tanto se concatenan
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10, 5)
my_result = sum_two_values (1.4, 5.2)
print (my_result)

def print_name (name, surname):
    print (f"{name} {surname}")

print_name (surname = "Gálvez", name ="Inma")

def print_name_with_default (name, surname, alias = "sin alias"):
    print (f"{name} {surname} {alias}")

print_name_with_default ("Inma", "Gálvez",)

def print_texts (*text): # de este dato puedo pasar los que quiera sólo por el asterisco
    print (text)
print_texts ("hola", "python", "azul" )

def print_texts (*texts):
    for text in texts:
        print(text.upper())
print_texts ("hola", "python", "azul" )
print_texts ("hola")