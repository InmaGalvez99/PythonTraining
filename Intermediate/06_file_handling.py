### FILE HANDLING 

import os 

# .txt file

txt_file = open("Intermediate/my_file.txt", "r") # para leer el archivo
txt_file.read()
print(txt_file.read())


txt_file = open("Intermediate/my_file.txt", "w") # para escribir el archivo 


txt_file = open("Intermediate/my_file.txt", "w+") # escribir y leer y sobreescribe
txt_file.read()

txt_file = open("Intermediate/my_file.txt", "r+") # leer y escribir
print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta SQL")
#txt_file.close()



# .json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test= {
    "name" :"Inma",
    "surnmae" : "Gálvez",
    "age": 23,
    "lenguage": "python"}

json.dump(json_test, json_file, indent = 4)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])



### .csv file

import csv


# .xml file

import xml