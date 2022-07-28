from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Suas opcpes: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
sleep(1)
print('=' * 20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=' * 20)
if computador == 0: #computador jogou PEDRA
    if jogador == 0: #jogador jogou PEDRA
        print('EMPATE!')
    elif jogador == 1: #jogador jogou PAPEL
        print('PARABENS, VOCE GANHOU!')
    elif jogador == 2: #jogador jogou TESOURA
        print('VOCE PERDEU! TENTE NOVAMENTE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0: #jogador jogou PEDRA
        print('VOCE PERDEU! TENTE NOVAMENTE!')
    elif jogador == 1: #jogador jogou PAPEL
        print('EMPATE!')
    elif jogador == 2: #jogador jogou TESOURA
        print('PARABENS, VOCE GANHOU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0: #jogador jogou PEDRA
        print('PARABENS, VOCE GANHOU!')
    elif jogador == 1: #jogador jogou PAPEL
        print('VOCE PERDEU! TENTE NOVAMENTE!')
    elif jogador == 2: #jogador jogou TESOURA
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
