'''
URL: https://aprendeconalf.es/docencia/python/retos/ajedrez/

La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del 
tablero están separadas por cambios de línea y las columnas por tabuladores.

El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario. Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. 
Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello 
añadirá el tablero resultante al final del fichero anterior.

El fichero partida-ajedrez.txt contiene un ejemplo con el fichero resultante de una partida con 3 movimientos.
'''

#Fichas
peonBlanco = "♙"
torreBlanco = "♖"
caballoBlanco = "♘"
alfilBlanco = "♗"
reyBlanco = "♕"
reinaBlanco = "♔"
peonNegro = "♟"
torreNegro = "♜"
caballoNegro = "♞"
alfilNegro = "♝"
reyNegro = "♛"
reinaNegro = "♚"

#Nombre del tablero
tableroName = input("Nombre del tablero: ")
tableroFile = tableroName + ".txt"

def tableroInical():
    #Borramos el contenido
    with open(tableroFile, "w") as txtFile:
        txtFile.write("")
        txtFile.close()

    #Añadimos el tablero
    with open(tableroFile, "a", encoding="utf-8") as txtFile:
        for i in range(1,9):  #Linea
            for n in range(1,9):  #Columna
                #Fichas
                if i == 2:
                    txtFile.write(peonBlanco)
                    txtFile.write("\t")
                elif i == 1 and n == 1 or i == 1 and n == 8:
                    txtFile.write(torreBlanco)
                    txtFile.write("\t")
                elif i == 1 and n == 2 or i == 1 and n == 7:
                    txtFile.write(caballoBlanco)
                    txtFile.write("\t")
                elif i == 1 and n == 3 or i == 1 and n == 6:
                    txtFile.write(alfilBlanco)
                    txtFile.write("\t")
                elif i == 1 and n == 4:
                    txtFile.write(reyBlanco)
                    txtFile.write("\t")
                elif i == 1 and n == 5:
                    txtFile.write(reinaBlanco)
                    txtFile.write("\t")
                elif i == 7:
                    txtFile.write(peonNegro)
                    txtFile.write("\t")
                elif i == 8 and n == 1 or i == 8 and n == 8:
                    txtFile.write(torreNegro)
                    txtFile.write("\t")
                elif i == 8 and n == 2 or i == 8 and n == 7:
                    txtFile.write(caballoNegro)
                    txtFile.write("\t")
                elif i == 8 and n == 3 or i == 8 and n == 6:
                    txtFile.write(alfilNegro)
                    txtFile.write("\t")
                elif i == 8 and n == 4:
                    txtFile.write(reyNegro)
                    txtFile.write("\t")
                elif i == 8 and n == 5:
                    txtFile.write(reinaNegro)
                    txtFile.write("\t")
                else:
                    txtFile.write("\t")
                #Saltar columnas
                if n == 8:
                    txtFile.write("\n")

        
tableroInical()