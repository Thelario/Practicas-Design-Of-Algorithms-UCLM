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

from PIL import Image
from matriz import matriz

# Encapsula algunas funciones que permiten trabajar con imágenes.
class imagen:
    # Crea una imagen vacía
    def __init__(self):
        self.imagen = None
        self.ancho = 0
        self.alto = 0
        
    # Carga la imagen desde un archivo.    
    def cargaArchivo(self, archivo):
        self.imagen = Image.open(archivo)
        self.ancho = self.imagen.size[0]
        self.alto = self.imagen.size[1]
        print ("Cargada imagen %s. (%d x %d pixeles)" % (archivo, self.ancho, self.alto))
        
    # Carga la imagen desde una matriz de tuplas (r,g,b)
    def cargaMatrizRGB(self, matrizRGB):
        self.alto = matrizRGB.numFilas()
        self.ancho = matrizRGB.numColumnas()
        self.imagen = Image.new("RGB", (self.ancho,self.alto))
        pixelsImagen = self.imagen.load();
        for fila in range(self.alto):
            for columna in range(self.ancho):
                pixelRGB = matrizRGB[(fila,columna)]
                pixelsImagen[columna,fila]=pixelRGB 
        print ("Creada imagen desde matriz. (%d x %d pixeles)" % (self.ancho, self.alto))                
        
    # Muestra la imagen
    def muestra(self):
        if not (self.imagen is None):
            self.imagen.show()
        else:
            print ("No se ha cargado ninguna imagen.")
            
    # Devuelve la matriz de colores. Para cada pixel devuelve una tupla
    # con tres enteros correspondientes a la componente roja, verde y azul del color.
    # mat[1,1] = (r,g,b)
    def matrizRGB(self):
        if self.imagen is None:
            print ("No se ha cargado ninguna imagen.")
            return
        # Extrae la imagen en formato "raw" (sin comprimir)
        imagen_rgb = self.imagen.convert('RGB')
        
        # Guarda en un objeto matriz la información.
        matrizRGB = matriz(self.alto, self.ancho)
        for fila in range(self.alto):
            for columna in range(self.ancho):
                (r,g,b)  =  imagen_rgb.getpixel((columna, fila)) # En las imágenes se referencia primero la columna.
                matrizRGB[(fila,columna)]=(r,g,b)
        return matrizRGB
        

        

            