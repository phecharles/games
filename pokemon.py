class Pokemon:

    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def atacar(self, pokemon):
        print('>>>> {} atacou {}'.format(self.especie, pokemon.especie))

meu_pokemon = Pokemon('Fogo', 'Charmander')
pokemon_amigo = Pokemon('Raio', 'Pikachu')

meu_pokemon.atacar(pokemon_amigo)