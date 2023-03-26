## CLASSES ##

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias ="sin alias"): #asignar atributos y realizar operaciones con el objeto (constructor)
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name #propiedad privada
        
    
    def get_name (self):
        return self.__name 
    
    def walk (self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Inma", "Gálvez")
print (my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person ("Inma", "Gálvez", "inmion")
print (my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print (my_other_person.full_name)