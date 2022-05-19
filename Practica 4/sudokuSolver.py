######################################################################################
# En la funcion leerTablero() vamos a proceder a meter en una matriz los datos del .txt
# primero, inicializamos una matriz, con todo a 0s, para luego trabajar con ella
# una vez esta inicializada, pasaremos a ir leyendo linea por linea el .txt en el cual
# hemos guardado la configuracion pervia del tablero, una vez hemos leido una linea,
# recorremos esa linea punto a punto para ir guardando el valor en la matriz 
######################################################################################

def leerTablero():

    archivo = open("sudoku.txt", mode="r") # Primero abrimos el archivo en modo lectura

    tablero = [[0,0,0,0,0,0,0,0,0], # Definimos el tablero con todo a 0s
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0]]

    r = 0
    c = 0
    for linea in archivo: # Este bucle recorre todas las lineas del txt una por una

        for c in range(len(linea)): # Una vez tenemos la linea, la recorremos de izquierda a derecha paso a paso

            if linea[c] == "\n": # Si es un salto de linea, pasamos
                continue

            if linea[c] == " ": # Si es un espacio ponemos un 0
                tablero[r][c] = 0
            else:
                tablero[r][c] = int(linea[c]) # El resto lo pasamos como numeros

        r += 1
    
    return tablero

######################################################################################
# La funcion resolverTablero intenta encontrar solucion al tablero que le llega como
# parametro, primero busca 0s, una vez la funcion encontrarCeros le retorna una
# posicion, prueba con todos los numeros posibles del 1 al 9, cada vez que prueba
# un numero, llama a valido, para ver si ese numero puede colocarse en base a las
# restricciones que tiene el sudoku, llegado el momento que recorremos el tablero
# en busca de 0s y no encontramos, hemos llegado a la solucion,
# si en algun momento, no podemos continuar, el bucle para con el return False final
# lo que indica que no hay solucion.
######################################################################################

def resolverTablero(tablero):

    encontrado = encontrarCeros(tablero)
    if not encontrado:
        return True
    else:
        row, col = encontrado

    for i in range(1,10):

        if valido(tablero, i, (row, col)):
            tablero[row][col] = i

            if resolverTablero(tablero):
                return True

            tablero[row][col] = 0

    return False

######################################################################################
# La funcion valido va a comprobar cada vez que resolverTablero encuentra un numero
# posible si este se puede colocar en base a las restricciones del sudoku
# las restricciones son que no puede aparecer ese numero ni en la misma fila, ni en
# la misma columna ni en el mismo cuadrante, entendiendo por cuadrante cada grupo de
# 3x3 que forman los numeros.
######################################################################################

def valido(tablero, num, pos):

    # Comprobar caja
    cajaX = pos[1] // 3
    cajaY = pos[0] // 3

    for i in range(cajaY * 3, cajaY * 3 + 3):
        for j in range(cajaX * 3, cajaX * 3 + 3):
            if tablero[i][j] == num and (i,j) != pos: # comprueba si en el cuadrante existe ya el numero, parecido a buscar en una matriz un numero
                return False

    # Comprobar fila
    for i in range(len(tablero[0])):
        if tablero[pos[0]][i] == num and pos[1] != i: # comprueba si en la fila existe ya el numero
            return False

    # Comprobar columna
    for i in range(len(tablero)):
        if tablero[i][pos[1]] == num and pos[0] != i: # comprueba si en la columna existe ya el numero
            return False

    return True

######################################################################################
# La funcion encontrarCeros recorre el tablero que se le pasa como parametro
# entero, en busca de 0s, recordad que al incinio, inicializamos el tablero
# a 0s, para ahora poder buscar mas facilmente la posicion,
# una vez encuentra la posicion, la retorna.
######################################################################################

def encontrarCeros(tablero):

    for i in range(len(tablero)):

        for j in range(len(tablero[0])):

            if tablero[i][j] == 0:
                return (i, j)  # fila, columna

    return None

######################################################################################
# La funcion imprimirTablero basicamente va a imprimir de una forma ordenada y mas
# visual el tablero, ira fila a fila y columna a columna imprimiendo el valor
# del tablero, poniendo algunos detalles para mejorar la visualizacion.
######################################################################################

def imprimirTablero(tablero): 

    for i in range(len(tablero)): # Este bucle recorre todo el tablero

        if i % 3 == 0 and i != 0 or i == 0: # cada 3 filas, incluyendo la 1a y la ultima, imprime una linea
            print("----------------------------")

        for j in range(len(tablero[0])): # cada 3 columnas, incluyendo la 1a y la ultima, imprime una linea

            if j % 3 == 0 and j != 0 or j == 0:
                print(" | ", end="")

            if j == 8:
                print(str(tablero[i][j]) + " |")
            else:
                print(str(tablero[i][j]) + " ", end="")
                
    print("----------------------------")

######################################################################################

tablero = leerTablero()
print("\n  TABLERO INICIAL A RESOLVER")
imprimirTablero(tablero)
resolverTablero(tablero)
print("\n  TABLERO FINAL RESUELTO")
imprimirTablero(tablero)