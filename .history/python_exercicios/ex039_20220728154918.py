from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
sexo = str(input('Qual seu sexo:'))
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    print('Seu alistamento sera em {}.'.format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alisatdo ha {} anos.'.format(saldo))
    print('Seu alistamento deveria ter ocorrido em {}.'.format(atual - saldo))



#Exercício Python 39: Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora exata de se
# alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.