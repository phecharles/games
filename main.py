import pickle
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

def salvar_jogo(player):
    try:
        with open("database", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Game salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar")
        print(error)

def carregar_jogo():
    try:
        with open("database", "rb") as arquivo:
            player = pickle.load(arquivo)
            return player
            print("Game carregado com sucesso!")
    except Exception as error:
        print("Erro ao carregar o game")
        print(error)

if __name__ == "__main__":
    print("====================================================")
    print("Bem-vindo ao Game Pokemon RPG de Terminal")
    print("====================================================")

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é o seu nome? ")
        player = Player(nome)
        print("{}, esse é um mundo habitado por Pokemons, sua missão é se tornaR um mestre de Pokemons!!".format(nome))
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns Pokemons")
            player.mostrar_pokemons()
        else:
            print("[ATENÇÃO]: Você não tem nenhum Pokemon, portanto você precisa escolher um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você possui um Pokemon, enfrente seu Inimigo Gary")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("====================================================")
        print("1- Explorar o mundo a fora")
        print("2- Lutar com um inimigo")
        print("3- Ver Pokeagenda")
        print("0 - Sair do jogo")
        escolha = input("Oque deseja fazer?")


        if escolha == "0":
            print("Fechando o joog")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            salvar_jogo(player)
        else:
            print("Escolha inválida")

