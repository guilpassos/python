from time import sleep
def lin():
    print('-=' * 20)


def maior(*num):
    cont = maior = 0
    lin()
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if maior == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(9, 7, 3, 6, 2)
maior(8, 3, 1, 9)
maior(1, 5, 2)
maior(6)
maior(0)


#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem
# que analisar todos os valores e dizer qual deles é o maior.