# coding: utf8
# La l��nea anterior tiene como objetivo que se puedan hacer comentarios en castellano (con tildes)
 
#######################################################
#######################################################
#                                                     #
#            Dise�o de Algoritmos                     #
#                                                     #
#            Pr�ctica 3                               #
#                                                     #
#            Autor:                                   #    
#                                                     #
#######################################################
#######################################################

from matriz import matriz

# Hace el seam carving sobre la matriz pasada como argumento.
def seamCarving(matrizRGB, numPixels):
    ancho = matrizRGB.numColumnas()
    # Se fija un máximo del 25% de columnas.
    if numPixels > 0.25 * ancho:
        print ("Solo se permite borrar un 25% de las columnas.")
        return matrizRGB
    
   
    # Elimina los pixeles de  uno en uno.
    matrizRes = matrizRGB
    for i in range(numPixels):
        matrizRes = elimina1PixelAncho(matrizRes)
    # Devuelve la matriz resultado
    return matrizRes


# Elimina 1 pixel de ancho y devuelve la matriz resultante
def elimina1PixelAncho(matrizRGB):
    #**********************************************
    # IMPLEMENTAR
    #
    # Calculamos la matriz de energías
    matEnergias = matrizEnergias(matrizRGB)
    
    # Obtenemos el camino mínimo
    costes, camino = caminoMinimo(matEnergias)
    
    # Eliminamos el camino de la matriz original
    matrizRGBReducida = eliminaCaminoVertical(matrizRGB, camino)
    
    # Devlvemos la matriz reducida.
    return matrizRGBReducida

    
    
# Esta funci�n ha de devolver el camino m��nimo (vertical) en una matriz.
# El camino m��nimo se expresa como una lista con tantos elementos como filas
# tiene la matriz, y en la que en cada posici�n contiene el ��ndice de la columna
# que corresponde al camino m��nimo.
# Por ejemplo, si el camino m��nimo es (0,0), (1,0), (2,1), (3,2) la funci�n ha de devolver [0,0,1,2]
# La funci�n devuelve tambi�n la matriz de estados.
def caminoMinimo(mat):
    camino = [0] * mat.numFilas()
    
    numFilas = mat.numFilas()
    numColumnas = mat.numColumnas()
    
    # Se crea una matriz de estados a partir de la matriz original. 
    # Para cada estado almacenamos una tupla (coste, origen), donde el origen
    # es la columna de la fila anterior desde la que se ha llegado, y coste el 
    # coste del camino m��nimo desde el origen.
    #
    # Por ejemplo, si tenemos la matriz:
    #     0 10 3
    #     2 7 2
    #
    # Una posible matriz de estados es:
    #     (0,0) (10,0) (3,0)
    #     (2,0) (7,0) (12,1)
    #
    # La tupla (12,1) significa que se ha llegado desde la columna 1 de la fila anterior, es decir, desde la posición (0,1). 
    # El coste total hasta llegar a la posici�n (1,2) de la matriz es 12 ( = 10 + 2) 
    listaCostes = [(0,0)]* (numFilas*numColumnas)
    costes = matriz(numFilas,numColumnas, listaCostes)

    # Calcula los costes y caminos.
    # **********************************************     
    # IMPLEMENTAR

    # - PRIMERO SE CALCULA LA FILA 0
    for col in range(0, numColumnas):
        listaCostes[col] = (mat[0,col], 0)


    # - LUEGO PARA CADA ELEMENTO SE CONSIDERAN LOS VECINOS DE LA FILA
    # - DE ARRIBA (PUEDEN SER 3 O 2 SI ES UN BORDE) Y SE ACTUALIZAN TANTO SU COSTE (MÍNIMO POSIBLE)
    # - Y DESDE QUÉ VECINO SE LLEGA

    # Recorremos una matriz, por lo que hay que usar dos bucles, uno para las columnas y otro para las filas.
    for fila in range(1, numFilas):
        for columna in range(0, numColumnas):
            
            # Comprobamos primero si la columna = 0, lo que quiere decir que estamos en la primera columna de la matriz, y por
            # lo tanto tenemos que comprobar los vecinos de arriba y arriba-derecha.
            if(columna == 0):

                # Calculamos el vecino de arriba
                vecino1 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + columna][0]

                # Calculamos el vecino de arriba-derecha.
                vecino2 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + (columna+1)][0]

                # Comprobamos cuál de los dos vecinos tiene menor valor, y actualizamos la lista de costes en función a esto. El índice que
                # actualizamos de la listaCostes se calcula con la misma fórmula que usamos en el método de elimina camino vertical:
                # fila * numeroColumnas + columna. Esta fórmula se utiliza principalmente para trabajar con matrices que están representadas
                # como una lista.
                if(vecino1 <= vecino2):
                    listaCostes[fila * numColumnas + columna] =  vecino1, columna
                else:
                    listaCostes[fila * numColumnas + columna] = vecino2, columna + 1

            # Comprbamos si la columna es la última de todas, lo que significa que tenemos que comprobar los vecinos de arriba y de
            # arriba-izquierda.
            elif(columna == numColumnas - 1):

                # Calculamos el vecino de arriba-izquierda.
                vecino1 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + (columna-1)][0]

                # Calculamos el mecino de arriba.
                vecino2 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + columna][0]

                # Comprobamos cuál de los dos vecinos tiene menor valor, y actualizamos la lista de costes en función a esto.
                if(vecino1 <= vecino2):
                    listaCostes[(fila) * numColumnas + columna] =  vecino1, columna - 1
                else:
                    listaCostes[(fila) * numColumnas + columna] = vecino2, columna

            # En caso de que la columna sea distinta de 0 o de numColumnas-1, eso quiere decir que la columna está entre otras dos columnas,
            # y por lo tanto tenemos que calcular tres vecinos, el de arriba, arriba-izquierda y arriba-derecha.
            else:

                # Vecino arriba-izquierda.
                vecino1 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + (columna-1)][0]
                
                # Vecino de arriba.
                vecino2 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + columna][0]

                # Vecino arriba-derecha.
                vecino3 = mat[fila, columna] + listaCostes[(fila-1) * numColumnas + (columna+1)][0]

                # Calculamos cuál de los tres vecinos es el que menor valor tiene, y actualizamos la listaCostes en función a esto.
                if(vecino1 <= vecino2 and vecino1 <= vecino3):
                    listaCostes[(fila) * numColumnas + columna] =  vecino1, columna - 1 # Vecino 1 es el de menor valor
                elif(vecino2 <= vecino1 and vecino2 <= vecino3):
                    listaCostes[(fila) * numColumnas + columna] = vecino2, columna # Vecino 2 es el de menor valor
                else:
                    listaCostes[(fila) * numColumnas + columna] = vecino3, columna + 1 # Vecino 3 es el de menor valor

    # Recupera el camino a partir de la matriz de costes
    # Primero recupera el la posici�n que contiene el mínimo
    # coste en la �ltima fila.
    minCostUltimaFila = costes[(numFilas-1,0)][0]
    minColUltimaFila = 0;
    for columna in range(1,numColumnas):
        if costes[(numFilas-1,columna)][0]<minCostUltimaFila:
            minCostUltimaFila = costes[(numFilas-1,columna)][0]
            minColUltimaFila = columna
    
    
    # Recupera el camino hacia arriba
    #**********************************************
    # IMPLEMENTAR

    # La columna con menos valor de la última fila ya está calculada arriba.
    camino[numFilas-1]=minColUltimaFila

    # Para cada fila (menos la última, que ya está calculada):
    for fila in range(1, numFilas):

        # Calculamos el coste mas pequeño de la última fila
        minCostUltimaFila = costes[(numFilas-fila,0)][0]
        minColUltimaFila = 0

        # Iteramos por cada columna.
        for columna in range(1,numColumnas):

            # Si el coste de la posicion de columna y fila es menor quen el coste que tenemos guardado, actualizamos.
            if costes[(numFilas-fila,columna)][0]<minCostUltimaFila:
                minCostUltimaFila = costes[(numFilas-fila,columna)][0]
                minColUltimaFila = columna

        # Una vez calculado el coste de mínimo, actualizamos el camino con la columna correspondiente.
        camino[numFilas-fila]=minColUltimaFila
    
    # Se devuelve tanto los costes como el camino calculado.         
    return (costes,camino)        
    
        
    
# Esta funci�n toma como parámetro una matriz y un camino (vertical) expresado como
# una lista en la que en cada posici�n corresponde a una fila, y contiene el �ndice de la columna
# que se ha de borrar.
# Por ejemplo, si el camino  es (0,0), (1,0), (2,1), (3,2) el camino
# se expresa como [0,0,1,2].

# La funci�n ha de hacer las comprobaciones pertinentes y devolver una nueva matriz.
# Por ejemplo:
 
#     mat  =
#             1  2  3  4
#             5  6  7  8
#             9  10 11 12
#             13 14 15 16

#    camino= [0,0,1,2]

#    nuevaMat =
#              2  3  4
#              6  7  8
#              9 11 12
#             13 14 16

def eliminaCaminoVertical(mat, camino):
    numFilas = mat.numFilas()
    numColumnas = mat.numColumnas()
    
    if len(camino)!=numFilas:
        print ("El camino no es correcto.")
        return
    
    # Copia los datos de la nueva matriz en una lista. 
    nuevosDatos = mat.listaDatos()[:]
    
    # Calcula las posiciones que ocupan en la lista los elementos que se van a eliminar y las almacena
    # en una lista denominada posEliminadas
    # En el ejemplo, el camino [0,0,1,2] se refiere a los elementos en las posiciones [0,4,9,13]    
    posEliminadas = []
    for fila in range(numFilas):
        if camino[fila]>numColumnas-1:
            print ("El camino no es correcto.")
            return mat   

        # Para poder saber cual es la posicion correcta del pixel que queremos eliminar, tenemos que tener en cuenta que estamos trabajando
        # con matrices. Para poder hacer esto usamos la fórmula siguiente: columna + fila * numColumnas. En nuestro caso, columna = camino[fila].
        pos = fila * numColumnas + camino[fila]
        posEliminadas.append(pos)
        
    # Eliminar las posiciones en posEliminadas de la lista nuevosDatos.
    # Hay eliminar desde el final para que el orden no se altere.
    for fila in range(numFilas):    

        # Una vez hemos calculado las posiciones que queremos que eliminar, tenemos que calcular este posicion pero esta vez con respecto a 
        # la lista de nuevosDatos. Esta posición será el elemento guardado en posEliminadas cuyo índice es [numFilas - 1 - fila]. Esto es debido
        # a que tenemos que iterar la lista desde el final. El -1 es para evitar index out of bounds error.
        posicion = posEliminadas[numFilas - 1 - fila]
        del nuevosDatos[posicion]
    
    # Se crea la nueva matriz y se devuelve.
    return matriz(numFilas, numColumnas-1, nuevosDatos)
        
        
# Devuelve la matriz de energias
def matrizEnergias(matrizRGB):
    numColumnas = matrizRGB.numColumnas()
    numFilas = matrizRGB.numFilas()
    datos = [0]*(numFilas*numColumnas)
    
    # Crea la matriz
    matrizEnergia = matriz(numFilas, numColumnas,datos)
    for fila in range(numFilas):
        for columna in range(numColumnas):
            matrizEnergia[(fila,columna)] = energia(matrizRGB,fila,columna)
    return matrizEnergia    


# Calcula la energ��a de un pixel.
def energia(matrizRGB, fila , columna):
    numColumnas = matrizRGB.numColumnas()
    numfilas = matrizRGB.numFilas()
    if columna<0 or fila<0 or columna>numColumnas-1 or fila>numfilas-1:
        print ("No existe ese pixel en la matriz.")
    
    # En los bordes, se pone una energ��a fija.
    if (columna==0) or (fila==0) or(columna==numColumnas-1) or (fila==numfilas-1):
        return 195075;
   
    # Se obtienen los colores (r,g,b) de los pixeles de arriba, abajo, izquierda y derecha
    pxArriba = matrizRGB[(fila-1,columna)]
    pxAbajo = matrizRGB[(fila+1,columna)]
    pxIzquierda = matrizRGB[(fila,columna-1)]
    pxDerecha = matrizRGB[(fila,columna+1)]
    
    # Cuadrado del gradiente horizontal.
    Rx = (pxIzquierda[0]-pxDerecha[0]) * (pxIzquierda[0]-pxDerecha[0]);
    Gx = (pxIzquierda[1]-pxDerecha[1]) * (pxIzquierda[1]-pxDerecha[1]);
    Bx = (pxIzquierda[2]-pxDerecha[2]) * (pxIzquierda[2]-pxDerecha[2]);  
    DeltaSqX = Rx + Gx + Bx;
    
    # Cuadrado del gradiente vertical.
    Ry = (pxArriba[0]-pxAbajo[0]) * (pxArriba[0]-pxAbajo[0]);
    Gy = (pxArriba[1]-pxAbajo[1]) * (pxArriba[1]-pxAbajo[1]);
    By = (pxArriba[2]-pxAbajo[2]) * (pxArriba[2]-pxAbajo[2]);  
    DeltaSqY = Ry + Gy + By;
        
    # Energ��a
    energia = DeltaSqX + DeltaSqY;
    
    return energia
       