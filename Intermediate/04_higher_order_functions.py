### HIGER ORDER FUNCTIONS 

def sum_one (value):
    return value + 1


def sum_five (value):
    return value + 5


def sum_two_values_and_one (first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print (sum_two_values_and_one(5,2, sum_one))
print(sum_two_values_and_one(5, 2,sum_five ))


### CLOSURES

def sum_ten (original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten (1)
print(add_closure(5))

## BUILT-IN HIGHER ORDER FUNCTIONS

numbers = [2,5,10,21,3,30]

# Map #  una función map siempre necesita un conjunto iterable (listas)
""" recorre todos los valores y ejecuta una función sobre ellos para modificar su valor """

def multiply_two (number):
    return number *2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number *2 , numbers)))


# Filter
 
""" recorre todos los valores y ejecuta una función que retorna true o false para saber como filtrar los valores
del iterado """

def filter_value(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_value, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Reduce (ya no forma parte de las funciones built-in)

[2,5,10,21,3,30]

"""Reduce function is not defined in the Python built-in function. 
So first, you should import the reduce function """

from functools import reduce 

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))