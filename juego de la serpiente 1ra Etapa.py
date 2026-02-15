# Tamaño del tablero


filas = 10
columnas = 20
serpiente = [[5,5]] # [Fila, Columna]
comida = [2,10]
direccion = "D" # Empieza moviendose a la derecha la serpiente es el movimiento inicial
juego = True

while juego:  # Con el while se repetira el juego una y otra vez 
    for i in range(filas):  # Aqui recorre con los dos for toda la cuadricula
        for j in range(columnas):
             if [i,j] == comida:# Aqui la comida imprime como "F"
                print ("F", end = "")
             elif [i,j] in serpiente: # Si la posicion esta en serpiente imprime "O" la cual es el  
                print("O", end = "") # El cuerpo de  la serpiente
             else:
                print(".", end = "")  # aqui se imprime todo el tablero
        print()
    print("W = arriba, S = abajo, A = izquierda, D = derecha y Q = salir")
    movimiento = input("Movimiento: ")
    movimiento = movimiento.upper()
    if movimiento == "W":
        direccion = "W"
    elif movimiento == "S":# Aqui defini los movmientos de la serpiente y Q para terminar el while
        direccion = "S"
    elif movimiento == "A":
        direccion = "A"
    elif movimiento == "D":
        direccion = "D"    
    elif movimiento == "Q": 
        print("Saliendo del juego")
        juego = False
    
                