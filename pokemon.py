import random

class Pokemon:
    def __init__(self, especie, level= random.randint(1,10), nome=None):
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} Lv{}".format(self.nome, self.level)

# O METODO STR FAZ A CLASSE AO SER CHAMADA NO PRINT, MOSTRAR STRINGS E VARIAVIEIS QUE VOCÊ SELECIONAR
# ENTÃO, QUANDO MEU POKEMON ATACA O O OPONENTE, O SELF FAZ COM QUE O NOME DO MEU POKEMON SEJA O PRIMEIRO, E O PARAMETRO POKEMON SEJA A 
# VARIAVEL Q TA NO STR

    def atacar(self, pokemon):
        print('{} atacou {}'.format(self, pokemon))


class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'
    def atacar(self, pokemon):
        print('{} Lançou um raio do trovão em {}'.format(self, pokemon))

class PokemonFogo(Pokemon):
     tipo = 'Fogo'
     def atacar(self, pokemon):
        print('{} Lançou uma bola de fogo em {}'.format(self, pokemon))

class PokemonAgua(Pokemon):
     tipo = 'Agua'
     def atacar(self, pokemon):
        print('{} Lançou um jato de água em {}'.format(self, pokemon))

# meupoke = PokemonEletrico('Pikachhu', nome='Sam')
# pokedeagua = PokemonAgua('buba')
# pokedeagua.atacar(meupoke)