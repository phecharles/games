import random
from pokemon import *

NOMES = ['Maria','Marcelo','Mauro','Alfredo','Joao','Victor','Guilherme',
         'Charles','Tatiana','Nick','Joao','Willian']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charmilion'),
    PokemonFogo('Sharizard'),
    PokemonEletrico('Zulu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Pikachu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Aguaman'),
    PokemonAgua('Jatodagua')
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[], saldo=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = saldo

    def __str__(self):
        return self.nome

    def mostrar_dinheiro(self):
        print('{} possui ${} em sua conta'.format(self, self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('{} ganhou ${} em sua conta'.format(self, quantidade))

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Mostrando Pokemons de {}:'.format(self))
            for index, pokemon in enumerate(self.pokemons):
                print('{} - {}'.format(index, pokemon))
        else:
            print('{} não possui Pokemons'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('Essse jogador não possui nenhum jogador para ser escolhido')


    def batalhar(self, pessoa):
        print('{} iniciou uma batalha com {}'.format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    self.mostrar_dinheiro()
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print('Essa batalha não pode ocorrer')

class Player(Pessoa):
    tipo = 'Player'

    def capturar_pokemons(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} foi capturado'.format(pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('Digite sua escolha: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} eu escolho você!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('Escolha invalida')
        else:
            print('ERRO: Essse jogador não possui nenhum jogador para ser escolhido')

class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for pokemon in range(1,6):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)

