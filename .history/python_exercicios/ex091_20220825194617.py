from random import randint
from time import
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 
        'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
