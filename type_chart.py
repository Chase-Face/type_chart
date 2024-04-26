import pypokedex

#def main():

input = input("pokemon or type: ")
#type = pypokedex.get(types=input)
pokemon = pypokedex.get(name=input)
print(pokemon.types)
    #print(strong_against())
    #print(weak_to())


#if __name__ == "__main__"