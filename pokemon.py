class Pokemon:

    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
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

meu_pokemon = Pokemon('Fogo', 'Charmander')
pokemon_amigo = Pokemon('Raio', 'Pikachu')

print(meu_pokemon)