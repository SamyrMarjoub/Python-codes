from pokemon import *
import random
NOMESPLAYER = ['Sam', 'Gary', 'Joe', 'James', 'Miau', 'Jessy', 'Puts']
NOMESNIMIGO = ['João', 'O MAGO', 'O CHUPA-CU',
               'Pedrinho do grau', 'ComiQuemLeu']
POKEINIMIGON = [PokemonAgua('Bubassauro'), PokemonFogo('Charmander', PokemonFogo(
    'Charizard', PokemonEletrico('Raichu', PokemonAgua('Vaporeon'))))]


class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMESPLAYER)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            for pokemons in eu.pokemons:
                print(pokemons)
        else:
            print('O {} não tem nenhum pokemon'.format(self.nome))


class Player(Pessoa):
    tipo = 'Player'

    def capturarpokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} Capturou {}'.format(self, pokemon))


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(6):
                pokemons.append(random.choice(POKEINIMIGON))

        super().__init__(nome=nome, pokemon=pokemons)
        


meu_pokemon = PokemonEletrico('Pikachu', nome='Amanda')
meu_pokemon2 = PokemonAgua('Bubassauro')
eu = Player(nome='Samir', pokemons=[meu_pokemon, meu_pokemon2])
pokemon_selvagem = PokemonFogo('Charizard')
print('Antes de capturar')
eu.mostrar_pokemons()
eu.capturarpokemon(pokemon_selvagem)
eu.mostrar_pokemons()
inimigo = Inimigo(nome='Jose')
eu.mostrar_pokemons()
print(inimigo.nomeInimigo)
