total = totmil = menor = cont = 0
barato = ''
print('-'*30)
print('{:^30}'.format('LOJA DO GUI'))
print('-'*30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if menor < preco:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
    if resp == 'N':
        break
print('-' * 30)
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}!')
print(f'Temos {totmil} produtos custando mais de R$1000.00!')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')



#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.