from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em número de 0 a 5! Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar o número
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS!!! Voce me venceu!!!')
else:
    print('GANHEI!!! Pensei no número {} e nao no {}'.format(computador, jogador))
   