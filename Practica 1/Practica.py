import time
import sorting
import random
import xlsxwriter

# Tres experimentos para cada algoritmo de ordenación (Burbuja, Selección, Inserción)

# Experimentos:
#   - Arrays en orden directo
#   - Arrays en orden inverso
#   - Arrays en orden aleatorio

# Para cada uno, diferentes tamaños desde 100 elementos hasta 2000 con incrementos de 100 en 100 (20 mediciones para cada caso).
# Para exp. directo en inverso hacer una muestra. Para exp. aleatorion tomar 10 muestras y hacer la media (para evitar influencias anómalas).
# El array a ordenar debe ser el mismo para cada algoritmo en cada experimento.

workbook = xlsxwriter.Workbook('practica_1.xlsx')
worksheet = workbook.add_worksheet()

directoBurbujaList = []
directoSeleccionList = []
directoInsercionList = []

inversoBurbujaList = []
inversoSeleccionList = []
inversoInsercionList = []

randomBurbujaList = []
randomSeleccionList = []
randomInsercionList = []

for i in range(100, 2100, 100):

    myList = []

    # Crear la lista a usar en cada iteración
    for n in range(i):
        num = random.randrange(0, i)
        myList.append(num)

    length = len(myList)

    directList = myList.copy()
    sorting.Burbuja(directList, length)

    inverseList = directList.copy()
    inverseList.reverse()

    randomList = myList.copy()

        # DIRECTO

    # Directo Burbuja
    directoBurbuja = directList.copy()
    t = time.time()
    sorting.Burbuja(directoBurbuja, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Directo Burbuja: " + str(t))
    directoBurbujaList.append(t)

    # Directo Selección
    directoSeleccion = directList.copy()
    t = time.time()
    sorting.Seleccion(directoSeleccion, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Directo Selección: " + str(t))
    directoSeleccionList.append(t)

    # Directo Inserción
    directoInsercion = directList.copy()
    t = time.time()
    sorting.Insercion(directoInsercion, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Directo Inserción: " + str(t))
    directoInsercionList.append(t)

    print("")

        # INVERSO

    # Inverso Burbuja
    inversoBurbuja = inverseList.copy()
    t = time.time()
    sorting.Burbuja(inversoBurbuja, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Inverso Burbuja: " + str(t))
    inversoBurbujaList.append(t)

    # Inverso Selección
    inversoSeleccion = inverseList.copy()
    t = time.time()
    sorting.Seleccion(inversoSeleccion, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Inverso Selección: " + str(t))
    inversoSeleccionList.append(t)

    # Directo Inserción
    inversoInsercion = inverseList.copy()
    t = time.time()
    sorting.Insercion(inversoInsercion, length)
    t = time.time() - t
    print("(" + str(i) + ") " + "Inverso Inserción: " + str(t))
    inversoInsercionList.append(t)

    print("")

        # RANDOM 

    # Random Burbuja
    x = 0
    for j in range(10):
        randomBurbujaAux = randomList.copy()
        t = time.time()
        sorting.Burbuja(randomBurbujaAux, length)
        t = time.time() - t
        x += t

    x = x / 10

    print("(" + str(i) + ") " + "Random Burbuja: " + str(x))
    randomBurbujaList.append(x)

    # Random Selección
    x = 0
    for j in range(10):
        randomSeleccionAux = randomList.copy()
        t = time.time()
        sorting.Seleccion(randomSeleccionAux, length)
        t = time.time() - t
        x += t

    x = x / 10

    print("(" + str(i) + ") " + "Random Seleccion: " + str(x))
    randomSeleccionList.append(x)

    # Directo Inserción
    x = 0
    for j in range(10):
        randomInsercionAux = randomList.copy()
        t = time.time()
        sorting.Insercion(randomInsercionAux, length)
        t = time.time() - t
        x += t

    x = x / 10

    print("(" + str(i) + ") " + "Random Insercion: " + str(x))
    randomInsercionList.append(x)

    print("")

row = 0
column = 0
for item in directoBurbujaList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 1
for item in directoSeleccionList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 2
for item in directoInsercionList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 3
for item in inversoBurbujaList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 4
for item in inversoSeleccionList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 5
for item in inversoInsercionList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 6
for item in randomBurbujaList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 7
for item in randomSeleccionList:
    worksheet.write(row, column, item)
    row += 1

row = 0
column = 8
for item in randomInsercionList:
    worksheet.write(row, column, item)
    row += 1

workbook.close()