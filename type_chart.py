import requests
from cache import load_cache, save_cache
from type_weaknesses import get_type_weaknesses

CACHE_FILE = "pokemon_cache.json"

def main():
    all_pokemon_types = load_cache(CACHE_FILE)  # Load data from cache or fetch from API
    if not all_pokemon_types:
        all_pokemon_types = get_all_pokemon_types()
        save_cache(all_pokemon_types, CACHE_FILE)  # Save fetched data to cache

    pokemon_name = input("Enter a Pokémon name: ").lower()
    if pokemon_name in all_pokemon_types:
        pokemon_types = all_pokemon_types[pokemon_name]
        pokemon_weaknesses = get_type_weaknesses(pokemon_types)
        if pokemon_weaknesses:
            print(f"{pokemon_name.capitalize()} is weak to:")
            for weakness in pokemon_weaknesses:
                print("-", weakness.capitalize())
        else:
            print(f"{pokemon_name.capitalize()} has no weaknesses!")
    else:
        print(f"{pokemon_name.capitalize()} not found in the Pokémon database.")

def get_pokemon_weaknesses(types):
    type_weaknesses = load_type_weaknesses()
    weaknesses = set()
    for pokemon_type in types:
        if pokemon_type in type_weaknesses:
            weaknesses.update(type_weaknesses[pokemon_type])
    return weaknesses

def load_type_weaknesses():
    # Define your type weaknesses dictionary here or load it from a file
    return {
        "fire": ["water", "rock"],
        "water": ["electric", "grass"],
        # Add more type weaknesses as needed
    }

def get_all_pokemon_types():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"  # Adjust the limit to fetch all Pokémon
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        all_pokemon_types = {}

        for pokemon in data.get("results", []):
            pokemon_name = pokemon.get("name")
            pokemon_url = pokemon.get("url")

            pokemon_data = requests.get(pokemon_url).json()
            types = [t["type"]["name"] for t in pokemon_data["types"]]
            all_pokemon_types[pokemon_name] = types

        return all_pokemon_types
    else:
        print("Error: API request failed.")
        return {}

if __name__ == "__main__":
    main()
