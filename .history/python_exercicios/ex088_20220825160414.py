from random import randint
from telnetlib import PRAGMA_HEARTBEAT
lista = []
cont = 0
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
lista.sort()
print('-' * 30)
print('          MEGA SENA          ')
print('-' * 30)
print(f'Os numeros sorteados foram: {lista}')













# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
# a criar palpites.O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.