import random
from pokemon import *

NOMES = ['Maria','Marcelo','Mauro','Alfredo','Joao','Victor','Guilherme',
         'Charles','Tatiana','Nick','Joao','Willian']

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Mostrando Pokemons de {}'.format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('{} não possui Pokemons'.format(self))

class Player(Pessoa):
    tipo = 'Player'

    def capturar_pokemons(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} foi capturado'.format(pokemon))

class Inimigo(Pessoa):
    tipo = 'Inimigo'

charmander = PokemonFogo('Fogo', 'Charmander')
pikachu = PokemonEletrico('Eletrico', 'Pikachu')

eu = Player()
print(eu.nome)