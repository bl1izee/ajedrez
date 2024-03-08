'''
URL: https://aprendeconalf.es/docencia/python/retos/ajedrez/

La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del 
tablero están separadas por cambios de línea y las columnas por tabuladores.

El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario. Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. 
Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello 
añadirá el tablero resultante al final del fichero anterior.

El fichero partida-ajedrez.txt contiene un ejemplo con el fichero resultante de una partida con 3 movimientos.
'''
#Nombre del tablero
tableroName = input("Nombre del tablero: ")
tableroFile = tableroName + ".txt"

def tableroInical():
    #Borramos el contenido
    with open(tableroFile, "w") as txtFile:
        txtFile.write("")
        txtFile.close()

    #Añadimos el tablero
    with open(tableroFile, "a") as txtFile:
        #Linea
        for i in range(0,8):
            #Columna
            for n in range(0,7):
                if i == 0 and n == 0 or i == 7 and n == 0 or i == 0 and n == 6 or i == 7 and n == 6:
                    txtFile.write('♜')
                txtFile.write("\t")
            if i != 7:
                txtFile.write("\n")

        
tableroInical()