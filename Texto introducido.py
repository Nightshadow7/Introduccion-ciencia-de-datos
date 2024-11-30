
# Descripción: Escribe un programa que analice un texto introducido por el
# usuario.
# El programa debe:
# ● Solicitar una frase o texto.
# ● Contar cuántas palabras contiene el texto.
# ● Identificar la palabra más larga y la más corta.
# ● Mostrar un listado de palabras únicas ordenadas alfabéticamente.
# Requisitos:
# ● Usar funciones para dividir y analizar las palabras del texto.
# ● Utilizar estructuras como listas y conjuntos.
# Ejemplo de palabra unicas ordenadas:
# El lenguaje de programación Python es muy poderoso y versátil

def solicitar_texto():
  texto = input("Por favor, introduce una frase o texto: ").strip()
  if not texto:
    print("El texto no puede estar vacío. Inténtalo de nuevo.")
    return solicitar_texto()
  return texto

def analizar_texto(texto):
  palabras = texto.split()
  total_palabras = len(palabras)
  palabra_mas_larga = max(palabras, key=len)
  palabra_mas_corta = min(palabras, key=len)
  palabras_unicas = sorted(set(palabras))
  return {
      "total_palabras": total_palabras,
      "palabra_mas_larga": palabra_mas_larga,
      "palabra_mas_corta": palabra_mas_corta,
      "palabras_unicas": palabras_unicas,
  }

def mostrar_resultados(analisis):
  print("\n--- Resultados del análisis ---")
  print(f"Cantidad total de palabras: {analisis['total_palabras']}")
  print(f"Palabra más larga: '{analisis['palabra_mas_larga']}'")
  print(f"Palabra más corta: '{analisis['palabra_mas_corta']}'")
  print(analisis['palabras_unicas'])
  print("Palabras únicas ordenadas alfabéticamente:")
  print(", ".join(analisis['palabras_unicas']))

# Programa principal
def main():
  texto = solicitar_texto()
  analisis = analizar_texto(texto)
  mostrar_resultados(analisis)

if __name__ == "__main__":
  main()
