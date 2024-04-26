import pypokedex
from type_weaknesses import type_weaknesses

def main():
    input_pokemon = input("Enter a Pokémon name or type: ")

    pokemon = pypokedex.get(name=input_pokemon)
    print("Types:", pokemon.types)

    weaknesses = weak_to(pokemon.types)
    print("Weaknesses:", weaknesses)

def weak_to(types):
    pokemon_weaknesses = []
    for t in types:
        if t in type_weaknesses:
            pokemon_weaknesses.extend(type_weaknesses[t])

    return pokemon_weaknesses

if __name__ == "__main__":
    main()
