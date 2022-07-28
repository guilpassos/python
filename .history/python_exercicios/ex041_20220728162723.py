from datetime import date
nome = str(input('Nome do atleta: '))
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta {}, nasceu em {} e tem {} anos.'.format(nome, ano, idade))
if idade <= 9:
    print('O atleta {}, nasceu em {} e tem {} anos.'.format(nome, ano, idade))
    print('CATEGORIA MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade > 19 and idade <= 25:
    print('CATEGORIA SENIOR')
elif idade > 25:
    print('CATEGORIA MASTER')


#Exercício Python 041: A Confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER