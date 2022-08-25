from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 
        'jogador4': randint(1, 6)}
ranking = ()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('===== RANKING DOS JOGADORES =====')
for i, v in enumerate(ranking):
    print(f'{i + 1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)

#Exercício Python 091: Crie um programa onde 4 jogadores joguem um
# dado e tenham resultados aleatórios. Guarde esses resultados 
# em um dicionário em Python. No final, coloque esse dicionário 
# em ordem, sabendo que o vencedor tirou o maior número no dado.