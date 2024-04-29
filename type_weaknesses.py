# Define type weaknesses
TYPE_WEAKNESSES = {
    "normal": [],
    "fire": ["water", "rock"],
    "water": ["electric", "grass"],
    "electric": ["ground"],
    "grass": ["fire"],
    "ice": ["fire"],
    "fighting": ["flying", "psychic"],
    "poison": ["ground", "psychic"],
    "ground": ["water", "grass", "ice"],
    "flying": ["electric", "ice", "rock"],
    "psychic": ["bug", "ghost", "dark"],
    "bug": ["fire", "flying", "rock"],
    "rock": ["water", "grass", "fighting", "ground", "steel"],
    "ghost": ["ghost", "dark"],
    "dragon": ["ice", "dragon", "fairy"],
    "dark": ["fighting", "bug", "fairy"],
    "steel": ["fire", "fighting", "ground"],
    "fairy": ["poison", "steel"],
}

def get_type_weaknesses(pokemon_types):
    weaknesses = set()
    for pokemon_type in pokemon_types:
        weaknesses.update(TYPE_WEAKNESSES.get(pokemon_type, []))
    return weaknesses
