import random
import time

# Datos iniciales de los Pokémon
pokemones = {
    "Pikachu": {
        "hp": 100,
        "ataques": {
            "Impactrueno": 20,
            "Cola de Hierro": 25,
            "Placaje": 15
        }
    },
    "Charmander": {
        "hp": 100,
        "ataques": {
            "Llamarada": 25,
            "Garra Rápida": 20,
            "Arañazo": 15
        }
    },
    "Bulbasaur": {
        "hp": 100,
        "ataques": {
            "Latigazo": 20,
            "Hoja Afilada": 25,
            "Placaje": 15
        }
    },
    "Squirtle": {
        "hp": 100,
        "ataques": {
            "Pistola Agua": 20,
            "Burbuja": 25,
            "Placaje": 15
        }
    }
}

def mostrar_estado(pokemon):
    """Muestra el estado del Pokémon."""
    print(f"{pokemon['nombre']} - HP: {pokemon['hp']}")

def elegir_pokemon(jugador):
    """Permite al jugador elegir un Pokémon."""
    print(f"\n{jugador}, elige tu Pokémon:")
    for i, nombre in enumerate(pokemones.keys(), 1):
        print(f"{i}. {nombre}")
    eleccion = int(input("Ingresa el número de tu elección: ")) - 1
    nombres = list(pokemones.keys())
    if 0 <= eleccion < len(nombres):
        nombre = nombres[eleccion]
        pokemon = pokemones[nombre].copy()
        pokemon["nombre"] = nombre
        return pokemon
    else:
        print("Selección inválida. Se elegirá un Pokémon aleatorio.")
        nombre = random.choice(nombres)
        pokemon = pokemones[nombre].copy()
        pokemon["nombre"] = nombre
        return pokemon

def turno_jugador(pokemon_jugador):
    """Turno del jugador para elegir ataque."""
    print("\nElige tu ataque:")
    for i, (ataque, daño) in enumerate(pokemon_jugador["ataques"].items(), 1):
        print(f"{i}. {ataque} (Daño: {daño})")
    
    eleccion = int(input("Ingresa el número del ataque: ")) - 1
    ataques = list(pokemon_jugador["ataques"].items())
    
    if 0 <= eleccion < len(ataques):
        ataque, daño = ataques[eleccion]
        print(f"\n¡{pokemon_jugador['nombre']} usó {ataque}!")
        return daño
    else:
        print("\nAtaque inválido. Perdiste el turno.")
        return 0

def turno_pc(pokemon_pc):
    """Turno de la computadora para elegir ataque."""
    ataques = list(pokemon_pc["ataques"].items())
    ataque, daño = random.choice(ataques)
    print(f"\n{pokemon_pc['nombre']} usó {ataque}!")
    return daño

def main():
    print("¡Comienza el combate Pokémon!")
    
    jugador = input("Ingresa tu nombre: ")
    print(f"\n¡Hola, {jugador}!")

    # El jugador elige un Pokémon
    pokemon_jugador = elegir_pokemon(jugador)
    print(f"\nHas elegido a {pokemon_jugador['nombre']}.")

    # La PC elige un Pokémon aleatorio
    pokemon_pc = elegir_pokemon("PC")
    print(f"\nLa PC ha elegido a {pokemon_pc['nombre']}.")
    
    mostrar_estado(pokemon_jugador)
    mostrar_estado(pokemon_pc)

    while pokemon_jugador["hp"] > 0 and pokemon_pc["hp"] > 0:
        # Turno del jugador
        print(f"\n--- Turno de {jugador} ---")
        daño = turno_jugador(pokemon_jugador)
        pokemon_pc["hp"] -= daño
        if pokemon_pc["hp"] <= 0:
            pokemon_pc["hp"] = 0
            print(f"\n¡Has derrotado a {pokemon_pc['nombre']}!")
            break
        mostrar_estado(pokemon_pc)

        time.sleep(1)  # Pausa para dramatismo

        # Turno de la PC
        print("\n--- Turno de la PC ---")
        daño = turno_pc(pokemon_pc)
        pokemon_jugador["hp"] -= daño
        if pokemon_jugador["hp"] <= 0:
            pokemon_jugador["hp"] = 0
            print(f"\n¡{pokemon_pc['nombre']} ha derrotado a {pokemon_jugador['nombre']}!")
            break
        mostrar_estado(pokemon_jugador)

        time.sleep(1)  # Pausa para dramatismo

    print("\n¡El combate ha terminado!")

if __name__ == "__main__":
    main()
