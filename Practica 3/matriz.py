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


# Implementa una matriz genérica de datos.
# Los datos se almacenan internamente en una lista.
class matriz:
        
    # Crea una matriz en la que todos los elementos son None.
    def __init__(self, filas, columnas, datos=None):
        self.filas = filas
        self.columnas = columnas
        self.tamano = filas * columnas
        if datos is None:
            self.datos = [None]*self.tamano
        elif (len(datos)==self.tamano):
            self.datos = datos  
        else:
            print ("Las dimensiones son inconsistentes")
            self.datos = [None]*self.tamano
               
         
    # Devuelve el número de filas.    
    def numFilas(self):
        return self.filas       
    
    # Devuelve el número de columnas
    def numColumnas(self):
        return self.columnas 
    
    # Devuelve el conjunto de datos.
    def listaDatos(self):
        return self.datos
                
    # Imprime la matriz    
    # Ejemplo: print mat
    def __repr__(self):
        textMatriz = ''
        idxElem = 0
        for f in range(self.filas):
            for c in range(self.columnas):
                textMatriz = textMatriz + str(self.datos[idxElem])+'\t'
                idxElem = idxElem + 1
            textMatriz = textMatriz + '\n'
        return textMatriz

    # Acceso a los items. elemento es una tupla (fila,columna)
    # Ejemplo: mat[(2,3)]
    def __getitem__(self,elemento):
        (fila,columna) = elemento 
        if (fila<0 or fila>self.filas-1):
            print ("Error: Intentando acceder a la fila %d (el rango válido es de 0 a %d)." % (fila, self.filas-1))
            return None
        if (columna<0 or columna>self.columnas-1):
            print ("Error: Intentando acceder a la columna %d (el rango válido es de 0 a %d)." % (fila, self.columnas-1))
            return None        
        return self.datos[fila*self.columnas + columna] 
    
    # Acceso a los items. elemento es una tupla (fila,columna)
    # Ejemplo: mat[(2,3)] = "prueba"
    def __setitem__(self, elemento,valor):
        (fila,columna) = elemento;
        self.datos[fila*self.columnas + columna]= valor            
    
        
# Permite comprobar la clase        
def test():            
    a = matriz(4,5)
    a[(0,0)]=('prueba')
    a[(1,3)]=3
    a[(2,2)]=(5.3,2)
    print (a)

#test()


