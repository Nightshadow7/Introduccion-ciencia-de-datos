# Funciones y Clases en Python
print("=== Funciones y Clases ===")

# Ejemplo de función sin parámetros ni retorno
def saludar():
  print("¡Hola, mundo!")

# Ejemplo de función con parámetros y retorno
def sumar(a, b):
  return a + b

# Ejemplo de función con parámetros por defecto
def presentar_persona(nombre, edad=30):
  print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Ejemplo de función lambda
multiplicar = lambda x, y: x * y

# Llamado a las funciones
print("\n=== Ejemplos de Funciones ===")
saludar()
resultado = sumar(5, 7)
print(f"La suma es: {resultado}")
presentar_persona("Juan", 25)
presentar_persona("María")  # Usa el valor por defecto para edad
print(f"Multiplicación con lambda: {multiplicar(4, 3)}")

# Ejemplo de una clase
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Ejemplo de una clase con un método adicional
class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return 3.1416 * self.radio ** 2

  def calcular_perimetro(self):
    return 2 * 3.1416 * self.radio

# Crear objetos y utilizar métodos
print("\n=== Ejemplos de Clases ===")
persona1 = Persona("Ana", 22)
persona1.saludar()

circulo1 = Circulo(5)
print(f"Área del círculo: {circulo1.calcular_area():.2f}")
print(f"Perímetro del círculo: {circulo1.calcular_perimetro():.2f}")
