# Manejo de Archivos en Python
print("=== Manejo de Archivos ===")

# Crear un archivo y escribir contenido
print("\nEscribiendo en un archivo...")
with open("archivo_ejemplo.txt", "w") as archivo:
    archivo.write("Línea 1: Hola, este es un archivo de ejemplo.\n")
    archivo.write("Línea 2: Python facilita el manejo de archivos.\n")

print("Archivo creado y escrito correctamente.")

# Leer el contenido del archivo
print("\nLeyendo el archivo completo...")
with open("archivo_ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Leer línea por línea
print("\nLeyendo el archivo línea por línea...")
with open("archivo_ejemplo.txt", "r") as archivo:
    for linea in archivo:
        print(f"Línea leída: {linea.strip()}")

# Agregar más contenido al archivo
print("\nAgregando contenido al archivo...")
with open("archivo_ejemplo.txt", "a") as archivo:
    archivo.write("Línea 3: Se agregó esta línea al archivo.\n")

# Confirmar el contenido actualizado
print("\nLeyendo contenido actualizado del archivo...")
with open("archivo_ejemplo.txt", "r") as archivo:
    contenido_actualizado = archivo.read()
    print("Contenido actualizado:")
    print(contenido_actualizado)

# Manejo de excepciones al trabajar con archivos
print("\nManejo de excepciones...")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")

# Estructuras de Datos Avanzadas en Python
print("=== Estructuras de Datos Avanzadas ===")

# Listas anidadas
print("\nListas anidadas:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz:")
for fila in matriz:
    print(fila)

# Pilas (Stack) usando listas
print("\nPila (Stack):")
pila = []
pila.append("Elemento 1")  # Agregar
pila.append("Elemento 2")
pila.append("Elemento 3")
print("Pila después de agregar:", pila)
pila.pop()  # Quitar el último elemento
print("Pila después de quitar el último elemento:", pila)

# Colas (Queue) usando collections.deque
from collections import deque
print("\nCola (Queue):")
cola = deque(["Cliente 1", "Cliente 2", "Cliente 3"])
print("Cola inicial:", list(cola))
cola.append("Cliente 4")  # Agregar al final
print("Cola después de agregar:", list(cola))
cola.popleft()  # Quitar el primero
print("Cola después de quitar el primero:", list(cola))

# Diccionarios anidados
print("\nDiccionarios anidados:")
usuarios = {
    "usuario1": {"nombre": "Ana", "edad": 30},
    "usuario2": {"nombre": "Luis", "edad": 25}
}
print("Información de usuarios:")
for usuario, datos in usuarios.items():
    print(f"{usuario}: {datos}")

# Operaciones con conjuntos
print("\nOperaciones con conjuntos:")
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
print(f"Unión: {conjunto_a | conjunto_b}")
print(f"Intersección: {conjunto_a & conjunto_b}")
print(f"Diferencia: {conjunto_a - conjunto_b}")
print(f"Diferencia simétrica: {conjunto_a ^ conjunto_b}")

# Uso de collections.Counter
from collections import Counter
print("\nUso de Counter:")
elementos = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
conteo = Counter(elementos)
print("Conteo de elementos:", conteo)

# Uso de collections.defaultdict
from collections import defaultdict
print("\nUso de defaultdict:")
default_dic = defaultdict(int)
default_dic["a"] += 1
default_dic["b"] += 2
print("Defaultdict:", dict(default_dic))
