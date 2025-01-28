# Rotar una Matriz 90° en Sentido Horario
# Dada una matriz cuadrada, escribe un programa que realice la
# rotación de 90 grados en sentido horario y muestre la matriz rotada.
# Instrucciones:
# Define una matriz cuadrada predefinida (puedes usar una de tamaño
# 3x3 o 4x4).
# Implementa una función que rote la matriz 90° en sentido horario.
# Imprime la matriz original y la matriz rotada.

# 1. Primera version usando la libreria numpy
import numpy as np

def crear_matriz_np(tamaño):
  """Crea una matriz cuadrada usando NumPy a partir de la entrada del usuario."""
  print("\nIngresa los valores de la matriz:")
  matriz = []
  for i in range(tamaño):
    fila = []
    for j in range(tamaño):
      dato = int(input(f"Elemento [{i+1}][{j+1}]: "))
      fila.append(dato)
    matriz.append(fila)
  return np.array(matriz)

def imprimir_matriz_np(matriz):
  """Imprime una matriz NumPy de forma ordenada."""
  print("\nMatriz:")
  for fila in matriz:
    print(list(fila))

# Programa principal
if __name__ == "__main__":
  tamaño = int(input("Ingresa el tamaño de la matriz cuadrada: "))
  matriz = crear_matriz_np(tamaño)
  imprimir_matriz_np(matriz)

  # Rota la matriz 90° en sentido horario usando NumPy
  matriz_rotada = np.rot90(matriz, k=-1)  # k=-1 para rotar en sentido horario
  imprimir_matriz_np(matriz_rotada)



# 2. Segunda manera sin usar librerias adicionales
def crear_matriz(tamaño):
  """Crea una matriz cuadrada ingresada por el usuario."""
  print("\nIngresa los valores de la matriz:")
  matriz = []
  for i in range(tamaño):
    fila = []
    for j in range(tamaño):
      dato = int(input(f"Elemento [{i+1}][{j+1}]: "))
      fila.append(dato)
    matriz.append(fila)
  return matriz

def imprimir_matriz(matriz):
  """Imprime una matriz de forma ordenada."""
  print("\nMatriz:")
  for fila in matriz:
    print(fila)

def rotar_matriz_90_horario(matriz):
  """Rota una matriz cuadrada 90 grados en sentido horario."""
  tamaño = len(matriz)
  matriz_rotada = [[0] * tamaño for _ in range(tamaño)]
  for i in range(tamaño):
    for j in range(tamaño):
      matriz_rotada[j][tamaño - 1 - i] = matriz[i][j]
  return matriz_rotada

# Programa principal
if __name__ == "__main__":
  tamaño = int(input("Ingresa el tamaño de la matriz cuadrada: "))
  matriz = crear_matriz(tamaño)
  imprimir_matriz(matriz)
  matriz_rotada = rotar_matriz_90_horario(matriz)
  imprimir_matriz(matriz_rotada)

