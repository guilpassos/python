time = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    resp = str(input())



print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


#Exercício Python 095: Aprimore o desafio 93 para que ele funcione
# com vários jogadores, incluindo um sistema de visualização 
# de detalhes do aproveitamento de cada jogador.

