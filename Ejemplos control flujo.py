# Estructuras de control en Python
print("=== Estructuras de Control ===")

# Condicionales: if-elif-else
print("\nEjemplo de if-elif-else:")
edad = 20
if edad < 18:
  print("Eres menor de edad.")
elif 18 <= edad < 65:
  print("Eres adulto.")
else:
  print("Eres adulto mayor.")

# Bucle while
print("\nEjemplo de while:")
contador = 0
while contador < 3:
  print(f"Contador: {contador}")
  contador += 1

# Bucle for con range
print("\nEjemplo de for con range:")
for i in range(3):
  print(f"Iteración: {i}")

# Bucle for iterando sobre una lista
print("\nEjemplo de for con listas:")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
  print(f"Fruta: {fruta}")

# Manejo de excepciones: try-except
print("\nEjemplo de try-except:")
try:
  resultado = 10 / 0
except ZeroDivisionError:
  print("Error: No se puede dividir entre cero.")

# Match-case (introducido en Python 3.10)
print("\nEjemplo de match-case:")
comando = "iniciar"
match comando:
  case "iniciar":
    print("Sistema iniciado.")
  case "detener":
    print("Sistema detenido.")
  case _:
    print("Comando no reconocido.")
