### LAMBDA 

sum_two_values = lambda  first_value, second_value: first_value + second_value
print(sum_two_values (2, 4))

multiply_values = lambda first_value, second_values : first_value * second_values - 3
print(multiply_values(2,4))


def sum_three_values(value):
    return lambda firts_value, second_values: firts_value + second_values + value

print= sum_three_values(5)(2,4)
