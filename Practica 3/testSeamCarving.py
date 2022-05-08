# coding: utf8
 
#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos                     #
#                                                     #
#            Práctica 3                               #
#                                                     #
#######################################################
#######################################################

from imagen import imagen
from seamcarving import seamCarving
from time import time          # Para poder medir tiempos

# Argumentos de prueba
nombreImagen = "original.jpg"
numPixels = 50

# Crea una imagen y la muestra.
original = imagen()
original.cargaArchivo(nombreImagen)
original.muestra()

# Devuelve la imagen como matriz de tuplas (r,g,b)
matrizOriginal = original.matrizRGB()

# Se hace seam carving a la matriz resultado. 
print ("Iniciando seamcarving.\n")
tInicio = time()
matrizResultado = seamCarving(matrizOriginal, numPixels)
tFinal = time()
print ("Proceso de escalado concluído.\n")
print ("Tiempo : "+ str(tFinal-tInicio)+"\n")

# Construye la imagen a partir de la matriz resultado y la muestra
escalada = imagen()
escalada.cargaMatrizRGB(matrizResultado)
escalada.muestra()
