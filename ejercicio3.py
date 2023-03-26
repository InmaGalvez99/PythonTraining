#Crea un función, que dado un año, indique el elemento y animal correspondiente
# en el ciclo sexagenario del zodíaco chino.


def chineseZodiac(year):
    elements = ["madera", "fuego", "tierra", "metal", "agua"]
    animals = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]
    
    if (year < 604) : 
        return "El ciclo sexagenario comenzó en el año 604."
    

    sexagenaryYear = (year - 4) % 60
    element = elements[int((sexagenaryYear % 10) / 2)]
    animal = animals[sexagenaryYear % 12]

    return str(year)+": "+element +" y "+animal


print(chineseZodiac(1956))

