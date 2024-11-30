# 1. Ejercicio de facturacion simple
# Descripción: Crea un programa que permita a un usuario generar una
# factura básica con múltiples 10 productos. El programa debe:
# ● Solicitar el nombre y el precio de cada producto.
# ● Calcular el total de la compra y aplicar un descuento del 10% si el total
# supera $100.
# ● Mostrar la factura con los nombres, precios y total final.
# Requisitos:
# ● Usar bucles para ingresar productos.
# ● Almacenar los productos en una lista o diccionario.
# ● Aplicar operaciones condicionales para calcular descuentos.

def solicitar_dato(tipo, mensaje, validacion=None):
  while True:
    try:
      dato = tipo(input(mensaje))
      if validacion and not validacion(dato):
        raise ValueError
      return dato
    except ValueError:
      print(f"Entrada inválida. Por favor, ingresa un dato válido.")

def ingresar_productos(cantidad):
  productos = []
  print("\n--- Ingreso de productos ---")
  for i in range(cantidad):
    print(f"\nProducto {i + 1}:")
    nombre = solicitar_dato(str, "Nombre del producto: ")
    precio = solicitar_dato(
      float,
      "Precio del producto (en USD): ",
      validacion=lambda x: x > 0
    )
    descuento = solicitar_dato(
      int,
      "Descuento del producto (en %, 0-100, donde 0 indica sin descuento): ",
      validacion=lambda x: 0 <= x <= 100
    )
    productos.append({"nombre": nombre, "precio": precio, "descuento": descuento})
  return productos

def calcular_factura(productos):
  valor_neto = sum(p["precio"] for p in productos)
  total_descuentos = sum(p["precio"] * (p["descuento"] / 100) for p in productos)
  valor_con_descuentos = valor_neto - total_descuentos
  # Aplicar descuento global si corresponde
  descuento_global = 0
  if valor_con_descuentos > 100:
    descuento_global = 0.1 * valor_con_descuentos
    valor_con_descuentos -= descuento_global
  return valor_neto, total_descuentos, descuento_global, valor_con_descuentos

def generar_factura(productos, valor_neto, total_descuentos, descuento_global, valor_con_descuentos):
  print("\n--- Factura ---")
  print(f"{'Producto':<20} {'Precio (USD)':>10} {'Descuento (%)':>15} {'Ahorro (USD)':>15}")
  print("-" * 60)
  for p in productos:
    ahorro = p["precio"] * (p["descuento"] / 100)
    print(f"{p['nombre']:<20} {p['precio']:>10.2f} {p['descuento']:>15} {ahorro:>15.2f}")
  print("-" * 60)
  print(f"{'Valor Neto:':<20} {valor_neto:>10.2f}")
  print(f"{'Ahorro Total:':<20} -{total_descuentos:>9.2f}")
  if descuento_global > 0:
    print(f"{'Descuento Global (10%):':<20} -{descuento_global:>9.2f}")
  print(f"{'Total Final:':<20} {valor_con_descuentos:>10.2f}")

# Programa principal
def main():
  print("Bienvenido al sistema de facturación simple.")
  # Solicitar cantidad de productos
  cantidad_productos = solicitar_dato(
    int, 
    "¿Cuántos productos deseas ingresar? ",
    validacion=lambda x: x > 0
  )
  # Ingreso de productos
  productos = ingresar_productos(cantidad_productos)
  # Cálculo de totales
  valor_neto, total_descuentos, descuento_global, valor_con_descuentos = calcular_factura(productos)
  # Generar factura
  generar_factura(productos, valor_neto, total_descuentos, descuento_global, valor_con_descuentos)

if __name__ == "__main__":
  main()
