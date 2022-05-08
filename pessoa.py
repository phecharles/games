from pokemon import *

class Pessoa:
    def __init__(self, nome, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Anonimo'

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)


class Player(Pessoa):
    tipo = 'Player'

class Inimigo(Pessoa):
    tipo = 'Inimigo'

charmander = PokemonFogo('Fogo', 'Charmander')
pikachu = PokemonEletrico('Eletrico', 'Pikachu')

eu = Player(nome='Charles', pokemons=[charmander, pikachu])

print(eu.nome)
eu.mostrar_pokemons()
