from random import randint
print('='*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*30)
vit = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip()[0].upper()
        print(f'Voce jogou {jogador} e o computador jogou {computador}. O total foi {total}.')
        print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU! PARABENS!!')
            print('=' * 50)
            vit += 1
        else:
            print('Voce PERDEU!')
            print('=' * 50)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU! PARABENS!!')
            print('=' * 50)
            vit += 1
        else:
            print('Voce PERDEU!')
            print('=' * 50)
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER. VOCE VENCEU {vit} VEZES!')




# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.