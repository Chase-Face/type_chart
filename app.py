from flask import Flask, request, render_template
from pypokedex import get
from type_weaknesses import dual_type_weaknesses, mono_type_weaknesses

app = Flask(__name__)

def main(pokemon_name):
    # Fetch Pokémon data using pypokedex
    pokemon = get(name=pokemon_name)

    types = pokemon.types  # Get the types of the Pokémon
    
    if dual(types):
        dual_type = "/".join(types)
        result = f"Dual-type Pokémon with types: {dual_type}\n"
        if dual_type in dual_type_weaknesses:
            result += "Weaknesses:\n"
            for weakness in dual_type_weaknesses[dual_type]:
                result += f"- {weakness}\n"
                
        else:
            # Check if the reverse order exists in the dictionary
            reversed_dual_type = "/".join(reversed(types))
            if reversed_dual_type in dual_type_weaknesses:
                result += f"Reversed dual type found: {reversed_dual_type}\n"
                result += "Weaknesses:\n"
                for weakness in dual_type_weaknesses[reversed_dual_type]:
                    result += f"- {weakness}\n"
                    
            else:
                result += "No weaknesses found.\n"
    else:
        result = "Monotype Pokémon\n"
        monotype = types[0]
        result += f"Type: {monotype}\n"
        if monotype in mono_type_weaknesses:
            result += "Weaknesses:\n"
            for weakness in mono_type_weaknesses[monotype]:
                result += f"- {weakness}\n"
        else:
            result += "No weaknesses found.\n"
    
    return result

def dual(types):
    return len(types) == 2

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        pokemon_name = request.form['pokemon_name'].lower()
        result = main(pokemon_name)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
