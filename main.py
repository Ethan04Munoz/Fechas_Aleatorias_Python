from random import randint
import os



file = open("fechas.txt","w")

while True:
    try:
        cantidad_fechas = int(input("¿Cuantas fechas quieres generar?\n"))
        break;
    except ValueError:
        print("No debes ingresar cosas que no sean numeros enteros\nPor favor vuelve a intentarlo\n")
        continue

#

for var in range(0,cantidad_fechas):
    
    #Creación de la fecha

    dia = randint(1,28)
    mes = randint(1,12)
    año = "2020"

    sdia = str(dia)
    smes = str(mes)

    fecha = sdia + "/" + smes + "/" + año
    #Escribe en el archivo la variable que contenga la fecha
    file.write(fecha + "\n\n")



file.close()