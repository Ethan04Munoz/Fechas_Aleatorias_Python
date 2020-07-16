from random import randint
import os



file = open("fechas.txt","w")

for var in range(0,100):
    
    #Creación de la fecha

    dia = randint(1,28)
    mes = randint(6,6)
    año = "2020"

    sdia = str(dia)
    smes = str(mes)

    fecha = sdia + "/" + smes + "/" + año
    #Escribe en el archivo la variable que contenga la fecha
    file.write(fecha + "\n")



file.close()