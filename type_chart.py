from type_weaknesses import *
from pypokedex import get

def main(pokemon_name):

    

    pokemon_name = input("Enter a Pokémon name: ").lower()

    # Fetch Pokémon data using pypokedex
    pokemon = get(name=pokemon_name)

    types = pokemon.types  # Get the types of the Pokémon
    
#weaknesses

    #dual type weaknesses

    if len(types) == 2:
        dual_type = "/".join(types)
        print(f"Dual-type Pokémon with types: {dual_type}")
        if dual_type in weaknesses:
            print("Weaknesses:")
            for weakness in weaknesses[dual_type]:
                print("-", weakness)
        else:

            # Check if the reverse order exists in the dict

            reversed_dual_type = "/".join(reversed(types))
            if reversed_dual_type in weaknesses:
                print("Weaknesses:")
                for weakness in weaknesses[reversed_dual_type]:
                    print("-", weakness)
            else:
                print("No weaknesses found.")

    #monotype weaknesses

    else:
        print("Monotype Pokémon")
        monotype = types[0]
        print(f"Type: {monotype}")
        if monotype in weaknesses:
            print("Weaknesses:")
            for weakness in weaknesses[monotype]:
                print("-", weakness)
        else:
            print("No weaknesses found.")

#resistances

    #monotype resistances

    if monotype in resistances:
        print("Resistances: ")
        for resistance in resistances[monotype]:
            print("-", resistance)

    #dual type resistances

    elif dual_type in resistances:  
        print("Resistances: ")
        for resistance in resistances[dual_type]:
            print("-", resistance)

    #check if the reversed order exist in dict

    elif reversed_dual_type in resistances:
        print("Resistances: ")
        for resistance in resistances[reversed_dual_type]:
            print("-", resistance)
    else:
        print("No resistances.")

#immunities

    #monotype immunities

    if monotype in immunities:
        print("Immunities: ")
        for immunity in immunities[monotype]:
            print("-", immunity)

    #dual type immunities

    elif dual_type in immunities:
        print("Immunities: ")
        for immunity in immunities[dual_type]:
            print("-", immunity)

    #check if the reversed order exist in dict

    elif reversed_dual_type in immunities:
        print("Immunities: ")
        for immunity in immunities[reversed_dual_type]:
            print("-", immunity)
    else:
        print("No immunities.")




if __name__ == "__main__":
    main()
