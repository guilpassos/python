from time import sleep
from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*10)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    jogador = str(input('Par ou impar? [P/I]')).strip()[0].upper()
    print('Computador esta escolhendo...')
    computador = randint(1, 10)
    sleep(1)
    soma = n + computador
    cont += 1
    print(f'Voce jogou {n} e o computador jogou {computador}. O total foi {soma}.')
    if soma % 0 and jogador in 'pP':
        print('VOCE VENCEU! PARABENS!!')
        print('Vamos jogar novamente...')
        cont += 1
        sleep(1)
    if soma % 0 and jogador in 'iI':
        break
    if soma:
print('VOCE PERDEU')
print('GAME OVER. VOCE VENCEU {} VEZES!')




# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.