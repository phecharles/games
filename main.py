from pessoa import *
from pokemon import *

def escolher_pokemon_inicial(player):
    print('Olá {} você possui 3 escolhas de Pokemons para iniciar sua jornada!'.format(player))

    pikachu = PokemonEletrico('Pikachi', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('1 - Pikachu')
    print('2 - Charmander')
    print('3 - Squirtle')

    while True:
        escolha = int(input('Digite sua escolha: '))

        if escolha == 1:
            player.capturar_pokemons(pikachu)
            break
        elif escolha == 2:
            player.capturar_pokemons(charmander)
            break
        elif escolha == 3:
            player.capturar_pokemons(squirtle)
            break
        else:
            print('Escolha inválida')


player = Player('Charles')

player.explorar()