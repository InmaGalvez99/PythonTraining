## MODULES ##

import my_module
my_module.sum(5, 3, 1)
my_module.printValue ("Hola python")


from my_module import printValue, sum
printValue ("Hola python")
sum(5, 3, 1)

import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE
print(PI_VALUE)