'''URL: https://aprendeconalf.es/docencia/python/retos/ajedrez/ '''

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

#Funciones
#Crear tablero
def tableroInical():
    #Borramos el contenido
    with open(tableroFile, "w") as txtFile:
        txtFile.write("")
        txtFile.close()

    #Añadimos el tablero
    with open(tableroFile, "a", encoding="utf-8") as txtFile:
        for i in range(1,11):  #Linea
            for n in range(1,11):  #Columna
                                #Letras
                if i  == 1:
                    if n == 2:
                        txtFile.write("a")
                    elif n == 3:
                        txtFile.write("b")
                    elif n == 4:
                        txtFile.write("c")
                    elif n == 5:
                        txtFile.write("d")
                    elif n == 6:
                        txtFile.write("e")
                    elif n == 7:
                        txtFile.write("f")
                    elif n == 8:
                        txtFile.write("g")
                    elif n == 9:
                        txtFile.write("h")
                    else:
                        pass
                #Números
                if n == 1:
                    if i == 2:
                        txtFile.write("1")
                    elif i == 3:
                        txtFile.write("2")
                    elif i == 4:
                        txtFile.write("3")
                    elif i == 5:
                        txtFile.write("4")
                    elif i == 6:
                        txtFile.write("5")
                    elif i == 7:
                        txtFile.write("6")
                    elif i == 8:
                        txtFile.write("7")
                    elif i == 9:
                        txtFile.write("8")
                    else:
                        pass

                #Fichas
                if i == 3 and n != 1 and n != 10:
                    txtFile.write(peonBlanco)
                    txtFile.write("\t")
                elif i == 2 and n == 2 or i == 2 and n == 9:
                    txtFile.write(torreBlanco)
                    txtFile.write("\t")
                elif i == 2 and n == 3 or i == 2 and n == 8:
                    txtFile.write(caballoBlanco)
                    txtFile.write("\t")
                elif i == 2 and n == 4 or i == 2 and n == 7:
                    txtFile.write(alfilBlanco)
                    txtFile.write("\t")
                elif i == 2 and n == 5:
                    txtFile.write(reyBlanco)
                    txtFile.write("\t")
                elif i == 2 and n == 6:
                    txtFile.write(reinaBlanco)
                    txtFile.write("\t")
                elif i == 8 and n != 1 and n != 10:
                    txtFile.write(peonNegro)
                    txtFile.write("\t")
                elif i == 9 and n == 2 or i == 9 and n == 9:
                    txtFile.write(torreNegro)
                    txtFile.write("\t")
                elif i == 9 and n == 3 or i == 9 and n == 8:
                    txtFile.write(caballoNegro)
                    txtFile.write("\t")
                elif i == 9 and n == 4 or i == 9 and n == 7:
                    txtFile.write(alfilNegro)
                    txtFile.write("\t")
                elif i == 9 and n == 5:
                    txtFile.write(reyNegro)
                    txtFile.write("\t")
                elif i == 9 and n == 6:
                    txtFile.write(reinaNegro)
                    txtFile.write("\t")
                else:
                    txtFile.write("\t")

                #Saltar columnas
                if n == 10:
                    txtFile.write("\n")
        txtFile.close()
        #imprimir tablero
        with open(tableroFile, "r", encoding="utf-8") as table:
            tablePrint = table.read()
            print("\n" + tablePrint)
            table.close()

#Panel de ayuda
def panelHelp():
    print("Fichas:\n -Torre\n -Caballo\n -Alfil\n -Rey\n -Reina\n -Peon")

#Nombre del tablero
tableroName = input("Nombre del tablero: ")
tableroFile = "tableroPy-" + tableroName + ".txt"
tableroInical()

#Partida
x = -1
while True:
    x+=1
    #Turno blanco y negro
    if x%2 == 0:
        print("Turno blanco")
    else:
        print("Turno negro")

    #Pregunta movimiento
    inputKey = input("¿Que ficha quieres mover? --> ")
    inputKey = inputKey.lower()

    #Panel de ayuda
    if inputKey == "help":
        panelHelp()
    
    #Movimiento
    if inputKey == "peon" and x%2 == 0:
        print("Cuantas cas")
    
