#Creacion de Arrays y Matrices
numeros = [1, 2, 3, 4, 5, 6 ]
print(numeros) #salida: [1, 2, 3, 4, 5, 6]

#Operaciones basicas con Arrays
#Acceso a elementos
array = [10, 20, 30]
print(array[1]) #salida: 20

# Agregar elementos
array.append(40)
print(array) #salida: [10, 20, 30, 40]

#Eliminar elementos
array.remove(40)
print(array) #salida: [10, 20, 30]

#crear y manipular un array 
array1 = [10, 3, 2, 4, 5, 6, 9, 8, 7, 1]

#sumar elementos
suma = 0
for i in array1:
  suma += i
print(f"la suma del array es: {suma}" ) # salida: 55

#Ordenamiento de array
array1.sort()
print(array1) #salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#operaciones basicas con matrices
#Acceso a elementos
matriz = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [10, 11, 12, 13, 14, 15]
]
print(matriz[0][1]) #salida: 2

matriz2 = [
  [1, 2],
  [3, 4]
]
print(matriz2[0][0]) #salida: 1

#Añadir elementos
matriz.append([16, 17, 18, 19, 20])
print(matriz) #salida: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

#Modificar elementos
matriz[0][1] = 9
print(matriz) #salida: [[1, 9, 3, 4, 5], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

#suma de filas en una matriz
for i, fila in enumerate(matriz):
  print(f"Suma de fila {i}: {sum(fila)}")

#suma de columnas en una matriz
for col in range(matriz[0]):
  suma_col = 0
  for fila in matriz:
    suma_col += fila[col]
  print(f"La suma de la columna {col} es : {suma_col}")

#ordenamiento de una matriz por filas
for fila in matriz:
  fila.sort()
print(matriz) #salida: [[1, 3, 4, 5, 9], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]