from type_weaknesses import dual_type_weaknesses, mono_type_weaknesses
from pypokedex import get

def main(pokemon_name):

    

    pokemon_name = input("Enter a Pokémon name: ").lower()

    # Fetch Pokémon data using pypokedex
    pokemon = get(name=pokemon_name)

    types = pokemon.types  # Get the types of the Pokémon
    
    if dual(types):
        dual_type = "/".join(types)
        print(f"Dual-type Pokémon with types: {dual_type}")
        if dual_type in dual_type_weaknesses:
            print("Weaknesses:")
            for weakness in dual_type_weaknesses[dual_type]:
                print("-", weakness)
                
        else:
            # Check if the reverse order exists in the dictionary
            reversed_dual_type = "/".join(reversed(types))
            if reversed_dual_type in dual_type_weaknesses:
                print(f"Reversed dual type found: {reversed_dual_type}")
                print("Weaknesses:")
                for weakness in dual_type_weaknesses[reversed_dual_type]:
                    print("-", weakness)
                    
            else:
                print("No weaknesses found.")
    else:
        print("Monotype Pokémon")
        monotype = types[0]
        print(f"Type: {monotype}")
        if monotype in mono_type_weaknesses:
            print("Weaknesses:")
            for weakness in mono_type_weaknesses[monotype]:
                print("-", weakness)
        else:
            print("No weaknesses found.")

def dual(types):
    return len(types) == 2

if __name__ == "__main__":
    main()
