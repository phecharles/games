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

eu = Player(nome='Charles', pokemons=[])

print(eu.nome)
eu.mostrar_pokemons()
eu.capturar_pokemons(charmander)
eu.mostrar_pokemons()
