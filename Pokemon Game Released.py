import json
import random
import time

class Movimiento:
  def __init__(self, nombre, tipo, poder, precision, pp):
    self.nombre = nombre
    self.tipo = tipo
    self.poder = poder if poder is not None else 0  # Valor predeterminado para ataques sin daño
    self.precision = precision
    self.pp = pp

  def usar(self):
    """Reduce el PP del movimiento en 1 si es posible."""
    if self.pp > 0:
      self.pp -= 1
      return True
    return False


class Pokemon:
  def __init__(self, nombre, tipos, hp, ataques):
    self.nombre = nombre
    self.tipos = tipos
    self.hp = hp
    self.ataques = ataques

  def mostrar_estado(self):
    print(f"{self.nombre} - Tipos: {', '.join(self.tipos)}, HP: {self.hp}")

  def recibir_daño(self, daño):
    self.hp = max(0, self.hp - daño)

  def elegir_ataque(self):
    ataques_disponibles = [ataque for ataque in self.ataques if ataque.pp > 0]
    return random.choice(ataques_disponibles) if ataques_disponibles else None


def cargar_movimientos(nombre_archivo):
  with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    return json.load(archivo)


def cargar_pokemones(nombre_archivo, movimientos):
  with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    pokemones_data = json.load(archivo)

  pokemones = {}
  for pokemon_data in pokemones_data:
    try:
      nombre = pokemon_data["name"]["english"]
      tipos = pokemon_data["type"]
      hp = pokemon_data["base"]["HP"]
      ataques = [
        Movimiento(mov["ename"], mov["type"], mov.get("power", 0), mov.get("accuracy", 100), mov["pp"])
        for mov in movimientos
        if mov["type"] in tipos
      ]
      pokemones[nombre] = Pokemon(nombre, tipos, hp, ataques)
    except KeyError as e:
      print(f"Error al procesar un Pokémon: {pokemon_data}. Falta la clave {e}.")
      continue

  return pokemones


def elegir_pokemon(jugador, pokemones):
  print(f"\n{jugador}, elige tu Pokémon:")
  nombres = list(pokemones.keys())
  for i, nombre in enumerate(nombres, 1):
    print(f"{i}. {nombre}")

  eleccion = int(input("Ingresa el número de tu elección: ")) - 1
  if 0 <= eleccion < len(nombres):
    return pokemones[nombres[eleccion]]
  else:
    print("Selección inválida. Se elegirá un Pokémon aleatorio.")
    return random.choice(list(pokemones.values()))


def calcular_daño(ataque, atacante, defensor, efectividades):
  """Calcula el daño basado en el ataque, tipos y efectividades."""
  multiplicador = 1
  for tipo_atacante in atacante.tipos:
    for tipo_defensor in defensor.tipos:
      multiplicador *= efectividades.get(tipo_atacante, {}).get(tipo_defensor, 1)
  poder = ataque.poder if ataque.poder is not None else 0
  daño = int(poder * multiplicador)
  print(f"{ataque.nombre} fue {multiplicador}x efectivo!")
  return daño


def turno_jugador(pokemon_jugador, pokemon_pc, efectividades):
  print("\nElige tu ataque:")
  for i, ataque in enumerate(pokemon_jugador.ataques, 1):
    print(f"{i}. {ataque.nombre} (Tipo: {ataque.tipo}, Daño: {ataque.poder}, PP: {ataque.pp})")

  eleccion = int(input("Ingresa el número del ataque: ")) - 1
  if 0 <= eleccion < len(pokemon_jugador.ataques):
    ataque = pokemon_jugador.ataques[eleccion]
    if ataque.usar():
      print(f"\n¡{pokemon_jugador.nombre} usó {ataque.nombre}!")
      return calcular_daño(ataque, pokemon_jugador, pokemon_pc, efectividades)
    else:
      print(f"{ataque.nombre} se quedó sin PP. Perdiste el turno.")
      return 0
  else:
    print("\nAtaque inválido. Perdiste el turno.")
    return 0


def turno_pc(pokemon_pc, pokemon_jugador, efectividades):
  ataque = pokemon_pc.elegir_ataque()
  if ataque and ataque.usar():
    print(f"\n{pokemon_pc.nombre} usó {ataque.nombre}! (Tipo: {ataque.tipo}, Daño Base: {ataque.poder})")
    return calcular_daño(ataque, pokemon_pc, pokemon_jugador, efectividades)
  else:
    print(f"{pokemon_pc.nombre} no tiene ataques disponibles. Perdiste el turno.")
    return 0

def main():
  movimientos = cargar_movimientos("MovimientosPokemones.json") # Verificar que la ruta y el nombre del archivo sea la misma, de lo contrario cambiarla; aca se encuentran todos y cada uno de los movimientos a usar
  pokemones = cargar_pokemones("ListaPokemones.json", movimientos) # Verificar que la ruta y el nombre del archivo sea la misma, de lo contrario cambiarla; aca se encuentra la lista de cada uno de los pokemos a usar

  efectividades = {
    "Fire": {"Grass": 2, "Water": 0.5},
    "Water": {"Fire": 2, "Grass": 0.5},
    "Grass": {"Water": 2, "Fire": 0.5},
    "Electric": {"Water": 2},
    # Añadir más efectividades según sea necesario
  }

  print("¡Comienza el combate Pokémon!")
  jugador = input("Ingresa tu nombre: ")
  print(f"\n¡Hola, {jugador}!")

  pokemon_jugador = elegir_pokemon(jugador, pokemones)
  print(f"\nHas elegido a {pokemon_jugador.nombre}.")

  pokemon_pc = random.choice(list(pokemones.values()))
  print(f"\nLa PC ha elegido a {pokemon_pc.nombre}.")

  pokemon_jugador.mostrar_estado()
  pokemon_pc.mostrar_estado()

  while pokemon_jugador.hp > 0 and pokemon_pc.hp > 0:
    print(f"\n--- Turno de {jugador} ---")
    daño = turno_jugador(pokemon_jugador, pokemon_pc, efectividades)
    pokemon_pc.recibir_daño(daño)
    if pokemon_pc.hp == 0:
      print(f"\n¡Has derrotado a {pokemon_pc.nombre}!")
      break
    pokemon_pc.mostrar_estado()

    time.sleep(1)

    print("\n--- Turno de la PC ---")
    daño = turno_pc(pokemon_pc, pokemon_jugador, efectividades)
    pokemon_jugador.recibir_daño(daño)
    if pokemon_jugador.hp == 0:
      print(f"\n¡{pokemon_pc.nombre} ha derrotado a {pokemon_jugador.nombre}!")
      break
    pokemon_jugador.mostrar_estado()

    time.sleep(1)

  print("\n¡El combate ha terminado!")

if __name__ == "__main__":
  main()
