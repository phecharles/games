import random


class Pokemon:

    def __init__(self, especie, level=random.randint(1,100), nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return '{}({})'.format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} atacou {}'.format(self.especie, pokemon.especie))

class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'
    def atacar(self, pokemon):
        print('{} lançou um raio do trovão em {}'.format(self, pokemon))

class PokemonAgua(Pokemon):
    tipo = 'Agua'
    def atacar(self, pokemon):
        print('{} lançou um jato de agua em {}'.format(self, pokemon))

class PokemonFogo(Pokemon):
    tipo = 'Fogo'
    def atacar(self, pokemon):
        print('{} lançou uma bola de fogo em {}'.format(self, pokemon))

pikachu = PokemonEletrico('Pikachu', 50)
charmander = PokemonFogo('Charmander', 30)
