from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em número de 0 a 5! Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS!!! Voce me venceu!!!')
else:
    print('GANHEI!!! Pensei no número {} e nao no {}'.format(computador, jogador))

   
   #Exercício Python 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.