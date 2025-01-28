# Variables y tipos de datos
print("=== Variables y Tipos de Datos ===")

# Entero (int)
edad = 25
print(f"Edad: {edad} (Tipo: {type(edad)})")

# Flotante (float)
altura = 1.75
print(f"Altura: {altura} (Tipo: {type(altura)})")

# Cadena de texto (str)
nombre = "Juan"
print(f"Nombre: {nombre} (Tipo: {type(nombre)})")

# Booleano (bool)
es_estudiante = True
print(f"¿Es estudiante?: {es_estudiante} (Tipo: {type(es_estudiante)})")

# Lista (list)
frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas} (Tipo: {type(frutas)})")

# Tupla (tuple)
numeros = (1, 2, 3)
print(f"Tupla de números: {numeros} (Tipo: {type(numeros)})")

# Diccionario (dict)
persona = {"nombre": "Juan", "edad": 25, "altura": 1.75}
print(f"Diccionario de persona: {persona} (Tipo: {type(persona)})")

# Conjunto (set)
colores = {"rojo", "verde", "azul"}
print(f"Conjunto de colores: {colores} (Tipo: {type(colores)})")

# Operadores
print("\n=== Operadores ===")

# Operadores aritméticos
a, b = 10, 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# Operadores de comparación
print(f"\n¿{a} es igual a {b}? {a == b}")
print(f"¿{a} es diferente de {b}? {a != b}")
print(f"¿{a} es mayor que {b}? {a > b}")
print(f"¿{a} es menor o igual a {b}? {a <= b}")

# Operadores lógicos
x, y = True, False
print(f"\nOperador AND: {x} and {y} = {x and y}")
print(f"Operador OR: {x} or {y} = {x or y}")
print(f"Operador NOT: not {x} = {not x}")
