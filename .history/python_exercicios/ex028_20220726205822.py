from calendar import c
from random import randint
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em número de 0 a 5! Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar o número
if jogador == jogador:
    print('PARABÉNS!!! Voce me venceu!!!')
else:
    print('GANHEI!!! Pensei no número {} e nao no {}'.format(computador, jogador))
    