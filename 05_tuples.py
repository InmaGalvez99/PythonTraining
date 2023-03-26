## TUPLES son inmutables

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.56, "Inma", "Gálvez", "inmion")
my_other_tuple = (28, 45, 50)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[2])
print(my_tuple[-3])
#print(my_tuple[5]) error no hay 5 elementos

print(my_tuple.count("Gálvez"))
print(my_tuple.index("Inma")) #posición

print(my_tuple + my_other_tuple)

my_sum_tuples = (my_tuple + my_other_tuple)
print(my_sum_tuples)

print(my_sum_tuples[3:6]) #coge los elemntos entre el 3 y 6 sin el 3, entonces coge 4-5-6 

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "ingal"
my_tuple.insert(1, "azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


