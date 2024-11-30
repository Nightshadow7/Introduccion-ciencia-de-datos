
# Condicionales 
numero = int(input(" Ingrese un numero: "))

if numero % 2 == 0:
  print("Es par.")
else:
  print("Es impar.")

# Bucles
for i in range(5):
  print(f"Número: {i}")

# Funciones
def saludar (nombre):
  return f"¡Hola, {nombre}!"

print(saludar("Ana"))